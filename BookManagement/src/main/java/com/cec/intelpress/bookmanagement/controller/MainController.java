package com.cec.intelpress.bookmanagement.controller;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.commons.CommonsMultipartFile;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.Chapter;
import com.cec.intelpress.bookmanagement.domain.PdfBook;
import com.cec.intelpress.bookmanagement.domain.TechnicalArticle;
import com.cec.intelpress.bookmanagement.service.ArticleService;
import com.cec.intelpress.bookmanagement.service.BookService;
import com.cec.intelpress.bookmanagement.service.ChapterService;
import com.cec.intelpress.bookmanagement.service.PdfBookService;
import com.cec.intelpress.bookmanagement.util.Util;

/**
 * Handles and retrieves person request
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
			mav.setViewName("/");
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
						try {
							article.getArticle().transferTo(dest);
						} catch (IllegalStateException e) {
							e.printStackTrace();
						} catch (IOException e) {
							e.printStackTrace();
						}
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
		return "redirect:/suggestedreading";

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
		mav.setViewName("bookmodal");

		return mav;
	}
	
	@RequestMapping(value = "/pdfconversion", method = RequestMethod.GET)
	public ModelAndView getPdfConversion(Model model) {
		ModelAndView mav = new ModelAndView();

		mav.setViewName("pdfconversion");
		return mav;
	}
	
	@RequestMapping(value = "/uploadPdf", method = RequestMethod.POST)
	public String postUploadPdf(@ModelAttribute("pdf") PdfBook book) throws Exception {
		System.out.println(book.getTitle());
		System.out.println(book.getAuthor());
		System.out.println(book.getIsbn());
		System.out.println(book.getPdf().getOriginalFilename());
		
		String orgName = book.getPdf().getOriginalFilename();
		String[] test = orgName.split("\\.");
		if(test.length >= 2) {
			String newName = String.valueOf(UUID.randomUUID()) +"."+test[1];
			
			//TODO: Dirty hacky please for the love of god change this later
			String filePath = Util.PDF_DIR + newName;
			
			//Confirm that the uploads dir exists
			Util.validatePdfs();
			if (test[1].equalsIgnoreCase("pdf")) {
				File dest = new File(filePath);
				try {
					book.getPdf().transferTo(dest);
				} catch (IllegalStateException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
				
				book.setPdf(null);
				book.setPdfFileName(newName);
				pdfService.add(book);
				System.out.println("Created PdfBook!");
			} 
		}
		return "redirect:/";
	}

}
