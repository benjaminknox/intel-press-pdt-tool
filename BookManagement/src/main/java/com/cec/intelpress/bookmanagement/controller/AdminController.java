package com.cec.intelpress.bookmanagement.controller;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import com.cec.intelpress.bookmanagement.service.UserService;

/**
 * Handles and retrieves person request
 */
@Controller
@RequestMapping("/admin")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class AdminController {

	protected static Logger logger = Logger.getLogger("AdminController");
	@Resource(name="UserService")
	private UserService userService;
	
}
