package com.cec.intelpress.bookmanagement.controller;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.UserService;

/**
 * Handles and retrieves person request
 */
@Controller
@RequestMapping("/")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class AdminController {

	protected static Logger logger = Logger.getLogger("AdminController");
	@Resource(name="UserService")
	private UserService userService;
	
	@RequestMapping(value = "/bookmanagement", method = RequestMethod.GET)
	public String getBookManagement(Model model) {
		return "bookmanagement";
	}
}
