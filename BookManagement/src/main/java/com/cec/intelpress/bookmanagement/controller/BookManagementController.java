package com.cec.intelpress.bookmanagement.controller;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.Chapter;
import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.ArticleService;
import com.cec.intelpress.bookmanagement.service.BookService;
import com.cec.intelpress.bookmanagement.service.ChapterService;
import com.cec.intelpress.bookmanagement.service.UserService;
import com.cec.intelpress.bookmanagement.util.Util;

/**
 * Handles and retrieves person request
 */
@Controller
@RequestMapping("/admin/bookmanagement")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class BookManagementController {

	protected static Logger logger = Logger
			.getLogger("BookManagementController");

	@Resource(name = "BookService")
	private BookService bookService;

	@Resource(name = "ChapterService")
	private ChapterService chapterService;
	
	@Resource(name = "ArticleService")
	private ArticleService articleService;
	
	@Resource(name = "UserService")
	private UserService userService;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getBookManagement(Model model) {

		ModelAndView mav = new ModelAndView();

		List<Book> allBooks = bookService.getAll();

		mav.addObject("books", allBooks);
		mav.setViewName("bookmanagement");

		return mav;
	}
	
	/**
	 * This displays the details about a book and allows for the creation of new chapters
	 * @param bookId
	 * @return
	 */
	@RequestMapping(value = "/chapters/{bookid}", method = RequestMethod.GET)
	public ModelAndView chapters(@PathVariable(value = "bookid") String bookId) {
		Book book = bookService.get(bookId);
		
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("chapters");
		mav.addObject("book", book);
		
		return mav;
	}
	
	/**
	 * This is used to add new chapters to existing books
	 * @param book
	 * @param result
	 * @return
	 * @throws Exception
	 */
	@RequestMapping(value = "/addChapter", method = RequestMethod.POST)
	public ModelAndView addChapter(@ModelAttribute("chapter") Chapter chapter,
			BindingResult result, @RequestParam(value = "book_id") String bookId) throws Exception {
			
			ModelAndView mav = new ModelAndView();
		
			Book book = bookService.get(bookId);
			chapter.setBook(book);
			chapterService.add(chapter);
			
			book.getBookChapters().add(chapter);
			bookService.edit(book);
			
			logger.info("Created Chapter ["+chapter.getName()+"] on book ["+book.getTitle()+"]");
			
			mav.setViewName("chapters");
			mav.addObject("book", book);
			
			return mav;
	}
	
	/**
	 * This is used to edit an existing chapter
	 * @param chapterid the chapter to edit
	 * @return
	 * @throws Exception
	 */
	@RequestMapping(value = "/editchapter/{chapterid}", method = RequestMethod.GET)
	public ModelAndView getEditChapter(@PathVariable(value = "chapterid") int chapterid) throws Exception {
			ModelAndView mav = new ModelAndView();
			Chapter chapter = chapterService.get(chapterid);
			mav.setViewName("editchapter");
			mav.addObject("chapter", chapter);
			return mav;
	}
	
	/**
	 * This is used to update an existing chapter
	 * @param chapterid the chapter to edit
	 * @return
	 * @throws Exception
	 */
	@RequestMapping(value = "/editchapter/{chapterid}", method = RequestMethod.POST)
	public String postEditChapter(@ModelAttribute("chapter") Chapter chapter, @PathVariable(value = "chapterid") int chapterid) throws Exception {
			chapterService.edit(chapter, chapterid);
			
			Chapter old = chapterService.get(chapterid);
			String bookId = old.getBook().getId();
			
			return "redirect:/admin/bookmanagement/chapters/"+bookId;
	}
	
	/**
	 * This allows an admin to assign a chapter to a given user
	 * @param chapter
	 * @param result
	 * @param bookId
	 * @return
	 * @throws Exception
	 */
	@RequestMapping(value = "/assignChapter/{chapterId}", method = RequestMethod.GET)
	public ModelAndView assignChapter(@PathVariable(value = "chapterId") int chapterId) throws Exception {
			
			ModelAndView mav = new ModelAndView();
			
			mav.setViewName("assignchapter");
			Chapter chapter = chapterService.get(chapterId);
			
			if(chapter != null) {
				mav.addObject("chapter", chapter);
				List<User> users = userService.getAll();
				mav.addObject("users", users);
			} else {
				List<Book> allBooks = bookService.getAll();
				mav.addObject("books", allBooks);
				mav.setViewName("bookmanagement");
			}
			
			return mav;
	}	
	
	@RequestMapping(value = "/assignChapter", method = RequestMethod.POST)
	public String postAssignChapter(@RequestParam(value = "chapterId") int chapterId, @RequestParam(value = "author") int author) throws Exception {

		Chapter chapter = chapterService.get(chapterId);
		User user = userService.get(author);
		
		if(chapter != null && user != null) {
			chapter.setAssignedUser(user);
			chapterService.edit(chapter);
		}
		
		return "redirect:/suggestedreading#success=2";
	}
	
	/**
	 * This is used to add new chapters to existing books
	 * @param book
	 * @param result
	 * @return
	 * @throws Exception
	 */
	@RequestMapping(value = "/deleteChapter/{chapterId}", method = RequestMethod.GET)
	public ModelAndView deleteChapter(@PathVariable(value = "chapterId") int chapterId) throws Exception {
			
			Chapter chapter = chapterService.get(chapterId);

			chapter.setArticle(null);
			Book book = chapter.getBook();
			book.getBookChapters().remove(chapter);
			bookService.edit(book);
			chapterService.delete(chapterId);
			ModelAndView mav = new ModelAndView();
			mav.setViewName("chapters");
			mav.addObject("book", book);
			return mav;
	}

	@RequestMapping(value = "/addbook", method = RequestMethod.POST)
	public ModelAndView addBook(@ModelAttribute("book") Book book,
			BindingResult result) throws Exception {

		ModelAndView mav = new ModelAndView();

		mav.setViewName("bookmanagement");
		String orgName = book.getBookcover().getOriginalFilename();
		String[] test = orgName.split("\\.");
		
		boolean validForm = true;
	    ArrayList<String> errors = new ArrayList<String>();

		/** Validation checks **/
		if(book.getTitle().equals("")){
			errors.add("Please enter a title");
			validForm = false;
		}
		if (book.getAuthor().equals("")) {
			errors.add("Please enter an author");
			validForm = false;
		}
		if(book.getPublisher().equals("")) {
			errors.add("Please enter a publisher");
			validForm = false;
		}
		if(book.getIsbn().equals("")){
			errors.add("Please enter an ISBN");
			validForm = false;
		}
		if(book.getDescription().equals("")){
			errors.add("Please enter a book description");
			validForm = false;
		}
		if(book.getCategory().equals("")){
			errors.add("Please enter the book category");
			validForm = false;
		}
		if(test.length < 2){
			errors.add("Please select a book cover");
			validForm = false;
		}
		if(book.getBuyurl().equals("")) {
			errors.add("Please enter the url of where to purchase this book");
			validForm = false;
		}
		/** End of Validation Checks! **/
		if(validForm) {
			String newName = String.valueOf(UUID.randomUUID()) +"."+test[1];
			
			//TODO: Dirty hacky please for the love of god change this later
			String filePath = Util.UPLOADS_DIR + newName;
			
			//Confirm that the uploads dir exists
			Util.validateUploads();
			
			File dest = new File(filePath);
			Util.writeFileToFileSystem(book.getBookcover(), dest);
			
			book.setBookcovername(newName);
			book.setBookcover(null);
			bookService.add(book);
			mav.addObject("status", "Succesfully created new book");
			logger.info("Added new book");
		}
		
		List<Book> books = bookService.getAll();
		mav.addObject("books", books);
		mav.addObject("errors", errors);
		return mav;

	}

	@RequestMapping(value = "/delbook/{bookid}", method = RequestMethod.GET)
	public String delBook(@PathVariable(value = "bookid") String bookId) {

		bookService.delete(bookId);
		return "redirect:/admin/bookmanagement/";
	}
	
	@RequestMapping(value = "/editbook/{bookid}", method = RequestMethod.GET)
	public ModelAndView getEditBook(@PathVariable(value = "bookid") String bookId) {
		ModelAndView mav = new ModelAndView();
		Book book = bookService.get(bookId);
		mav.addObject("book", book);
		mav.setViewName("editbook");
		return mav;
	}
	
	@RequestMapping(value = "/editbook/{bookid}", method = RequestMethod.POST)
	public String postEditBook(@PathVariable(value = "bookid") String bookId, @ModelAttribute("book") Book book,
			BindingResult result) throws Exception {

		String orgName = book.getBookcover().getOriginalFilename();
		String[] test = orgName.split("\\.");
		
		//Make sure they selected a file
		if(test.length > 1) {
			String newName = String.valueOf(UUID.randomUUID()) +"."+test[1];
			
			//TODO: Dirty hacky please for the love of god change this later
			String filePath = Util.UPLOADS_DIR + newName;
			
			//Confirm that the uploads dir exists
			Util.validateUploads();
			
			File dest = new File(filePath);
			Util.writeFileToFileSystem(book.getBookcover(), dest);
			
			book.setBookcovername(newName);
			book.setBookcover(null);
			
			bookService.edit(book, bookId);
	
			logger.info("Updated book!");
			
			return "redirect:/admin/bookmanagement/";
		} else {
			return "redirect:/admin/bookmanagement/editbook/"+bookId+"#error=1";
		}
	}

}
