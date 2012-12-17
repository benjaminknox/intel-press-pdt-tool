package com.cec.intelpress.bookmanagement.controller;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.multipart.commons.CommonsMultipartFile;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.Chapter;
import com.cec.intelpress.bookmanagement.domain.PdfBook;
import com.cec.intelpress.bookmanagement.domain.TechnicalArticle;
import com.cec.intelpress.bookmanagement.service.ArticleService;
import com.cec.intelpress.bookmanagement.service.BookService;
import com.cec.intelpress.bookmanagement.service.ChapterService;
import com.cec.intelpress.bookmanagement.service.EmailService;
import com.cec.intelpress.bookmanagement.service.PdfBookService;
import com.cec.intelpress.bookmanagement.service.UserService;
import com.cec.intelpress.bookmanagement.util.Util;

/**
 * Handles and retrieves person request
 * @param <HttpServletResponse>
 */
@Controller
@RequestMapping("/")
@PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_USER')")
public class MainController {

	protected static Logger logger = Logger.getLogger("MainController");
	
	@Resource(name="BookService")
	private BookService bookService;
	
	@Resource(name="ChapterService")
	private ChapterService chapterService;
	
	@Resource(name="ArticleService")
	private ArticleService articleService;
	
	@Resource(name="PdfBookService")
	private PdfBookService pdfService;
	
	@Resource(name="UserService")
	private UserService userService;
	
	@Resource(name="emailService")
	private EmailService emailService;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getMain(Model model) {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("index");
		
		
		int uncompletedTechnicalChapters =  chapterService.getAllWithoutArticles().size();
		int totalArticles = articleService.getAll().size();
		int totalRequired = uncompletedTechnicalChapters + totalArticles;
		float percentDecimal = ((float)totalArticles)/((float)totalRequired);
		float percent = percentDecimal*100;
		
		//TODO: This is super inefficient, in the future let the db count it
		mav.addObject("bookCount", bookService.getAll().size());
		mav.addObject("uncompletedArticles", uncompletedTechnicalChapters);
		mav.addObject("totalArticles", totalArticles);
		mav.addObject("progress", percent);
		mav.addObject("chapterCount", chapterService.getAll().size());
		
		return mav;
	}
	
	@RequestMapping(value = "/uploadArticle/{chapterId}", method = RequestMethod.GET)
	public ModelAndView uploadArticle(@PathVariable(value = "chapterId") int chapterId) {
		Chapter chapter = chapterService.get(chapterId);
		ModelAndView mav = new ModelAndView();
		if(chapter != null) {
			mav.setViewName("uploadArticle");
			mav.addObject("chapter", chapter);
		}
		else {
			mav.setViewName("suggestedreading");
		}
		return mav;
	}
	
	@RequestMapping(value = "/addArticle/{chapterId}", method = RequestMethod.POST)
	public String addArticle(@ModelAttribute("article") TechnicalArticle article, @PathVariable(value = "chapterId") int chapterId) throws Exception {
		if (article != null) {
			CommonsMultipartFile articleFile = article.getArticle();
			if (articleFile != null) {
				String orgName = article.getArticle().getOriginalFilename();
				//TODO: This, and everything that looks like this is 100% vaulnrable to many bad things
				String[] test = orgName.split("\\.");
				if(test.length >= 2 && !article.getTitle().equals("")) {
					String newName = String.valueOf(UUID.randomUUID()) +"."+test[1];
					
					//TODO: Dirty hacky please for the love of god change this later
					String filePath = Util.UPLOADS_DIR + newName;
					
					//Confirm that the uploads dir exists
					Util.validateUploads();
					
					if (Util.validArticleExtensions.contains(test[1])) {
						File dest = new File(filePath);
						Util.writeFileToFileSystem(article.getArticle(), dest);

						Chapter chapter = chapterService.get(chapterId);
						if (chapter != null) {
							article.setArticleName(newName);
							article.setArticle(null);
							articleService.add(article);
					
							logger.info("~~~~~~~ Created Article  ["+article.getId()+"] ~~~~~~~~~~~");
							
							chapter.setArticle(article);
							chapterService.edit(chapter);
						}
					} else {
						return "redirect:/uploadArticle/"+chapterId+"#error=1";
					}
				} else {
					return "redirect:/uploadArticle/"+chapterId+"#error=2";
				}
			} else {
				return "redirect:/uploadArticle/"+chapterId+"#error=3";
			}
		}
		return "redirect:/suggestedreading#success=1";

	}
	
	@RequestMapping(value = "/suggestedreading", method = RequestMethod.GET)
	public ModelAndView getSuggestedReading(Model model) {
		ModelAndView mav = new ModelAndView();

		List<Book> allBooks = bookService.getAllSuggested();
		
		mav.addObject("suggestedBooks", allBooks);
		mav.setViewName("suggestedreading");
		return mav;
	}
	
	@RequestMapping(value="/getBook/{bookid}", method = RequestMethod.GET)
	public ModelAndView getBook(@PathVariable(value="bookid") String bookId)
	{
		ModelAndView mav = new ModelAndView();
		mav.addObject("book", bookService.get(bookId));
	    User user = (User)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
	    String name = user.getUsername(); //get logged in username
	    com.cec.intelpress.bookmanagement.domain.User realUser = userService.getUserByUserName(name);
	    mav.addObject("user", realUser);
		mav.setViewName("bookmodal");

		return mav;
	}
	
	@PreAuthorize("permitAll")
	@RequestMapping(value = "/finishedconvert/{pdfid}", method = RequestMethod.GET)
	public String getFinishedConvert(@PathVariable(value="pdfid") String pdfid) {
		PdfBook pdf = pdfService.get(pdfid);
		pdf.setConverted(true);
		pdfService.edit(pdf);
		emailService.sendPdfEmail(pdf);
		System.out.println("Got feedback from the converter!! Email should be inc!");
		return "redirect:/";
	}
	
	@PreAuthorize("permitAll")
	@RequestMapping(value = "/downloadepub/{pdfid}", method = RequestMethod.GET)
	public String getdownloadPdfBook(@PathVariable(value="pdfid") String pdfid) {
		PdfBook pdf = pdfService.get(pdfid);
		String pdfFile = (pdf.getPdfFileName().split("\\.(?=[^\\.]+$)"))[0];
        return "redirect:/pdfs/"+pdfFile+"."+pdf.getFormat();
		
	}
	
	@RequestMapping(value = "/pdfconversion", method = RequestMethod.GET)
	public ModelAndView getPdfConversion(Model model) {
		ModelAndView mav = new ModelAndView();
		if(!Util.TestForPdfServer()) {
			mav.addObject("serverStatus", false);
		}
		mav.setViewName("pdfconversion");
		return mav;
	}
	
	@RequestMapping(value = "/pastpdf", method = RequestMethod.GET)
	public ModelAndView getPastPdf(Model model) {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("pastpdf");
		
		User user = (User)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		String name = user.getUsername(); //get logged in username
		com.cec.intelpress.bookmanagement.domain.User realUser = userService.getUserByUserName(name);
		List<PdfBook> comppdfs = pdfService.getAllCompletedBooksByUser(realUser);
		mav.addObject("completedPdfs", comppdfs);
		return mav;
	}
	
	@RequestMapping(value = "/pendingpdf", method = RequestMethod.GET)
	public ModelAndView getPendingPdf(Model model) {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("pendingpdf");
		
		User user = (User)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		String name = user.getUsername(); //get logged in username
		com.cec.intelpress.bookmanagement.domain.User realUser = userService.getUserByUserName(name);
		List<PdfBook> nonpdfs = pdfService.getAllNonCompletedBooksByUser(realUser);
		mav.addObject("noncompletedPdfs", nonpdfs);
		return mav;
	}
	
	@RequestMapping(value = "/uploadPdf", method = RequestMethod.POST)
	public ModelAndView postUploadPdf(@ModelAttribute("pdf") PdfBook book) throws Exception {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("pdfconversion");

		String orgName = book.getPdf().getOriginalFilename();
		String[] test = orgName.split("\\.");
		
		//Get current logged in user
		User user = (User)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
	    String name = user.getUsername(); //get logged in username
	    com.cec.intelpress.bookmanagement.domain.User realUser = userService.getUserByUserName(name);
	    
	    ArrayList<String> errors = new ArrayList<String>();
	    
	    boolean validForm = true;
	    
	    //Perform validation checks
		if(test.length < 2) {
			errors.add("Please upload a pdf file");
			validForm = false;
		} else {
			if (!test[1].equalsIgnoreCase("pdf")) {
				errors.add("Invalid file type");
				validForm = false;
			}
		}
		if(book.getTitle().equals("")) {
			errors.add("Please enter a title");
			validForm = false;
		}
		if (book.getAuthor().equals("")) {
			errors.add("Please enter an author");
			validForm = false;
		}
		if (book.getEmail().equals("")){
			errors.add("Please enter a contact email");
			validForm = false;
		}
		if (book.getFormat().equals("")) {
			errors.add("Please select a format");
			validForm = false;
		}
		if(!Util.TestForPdfServer()) {
			mav.addObject("status", false);
			validForm = false;
		}
	
		//If validation has passed, lets do this!
		if(validForm) {
			String newName = String.valueOf(UUID.randomUUID()) +"."+test[1];
			
			//TODO: Dirty hacky please for the love of god change this later
			String filePath = Util.PDF_DIR + newName;
			
			//Confirm that the uploads dir exists
			Util.validatePdfs();
			File dest = new File(filePath);
			
			Util.writeFileToFileSystem(book.getPdf(), dest);
	
			book.setPdf(null);
			book.setPdfFileName(newName);
			book.setUploader(realUser);
			pdfService.add(book);
			
			//Attempt to convert PDF
			Util.sendPdfToServer(dest, book);
			mav.addObject("success", true);
		} else {
			mav.addObject("errors", errors);
		}
		return mav;
	}

}
