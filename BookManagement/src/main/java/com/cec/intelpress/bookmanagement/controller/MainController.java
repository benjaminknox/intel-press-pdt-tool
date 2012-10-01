package com.cec.intelpress.bookmanagement.controller;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
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
@RequestMapping("/")
@PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_USER')")
public class MainController {

	protected static Logger logger = Logger.getLogger("MainController");
	
	@Resource(name="BookService")
	private BookService bookService;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String getMain(Model model) {
		return "index";
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
	public ModelAndView getBook(@PathVariable(value="bookid") int bookId)
	{
		ModelAndView mav = new ModelAndView();
		mav.addObject("book", bookService.get(bookId));
		mav.setViewName("bookmodal");

		return mav;
	}


}
