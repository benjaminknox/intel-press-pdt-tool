package com.cec.intelpress.bookmanagement.controller;

import java.util.List;

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
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.service.BookService;

/**
 * Handles and retrieves person request
 */
@Controller
@RequestMapping("/admin/bookmanagement")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class BookManagementController {

	protected static Logger logger = Logger.getLogger("BookManagementController");
	@Resource(name="BookService")
	private BookService bookService;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getBookManagement(Model model) {
		
		ModelAndView mav = new ModelAndView();

		List<Book> allBooks = bookService.getAll();
		
		mav.addObject("books", allBooks);
		mav.setViewName("bookmanagement");
		
		return mav;
	}
	
	@RequestMapping(value = "/addbook", method = RequestMethod.POST)
	public String addBook(@ModelAttribute("book") Book book,
			BindingResult result) {
		
		bookService.add(book);
		logger.info("Added new book");
		
		return "redirect:/admin/bookmanagement/";
	}
	
	@RequestMapping(value = "/delbook/{bookid}", method = RequestMethod.GET)
	public String delBook(@PathVariable(value = "bookid") int bookId) {
		
		bookService.delete(bookId);
		return "redirect:/admin/bookmanagement/";
	}
	
}
