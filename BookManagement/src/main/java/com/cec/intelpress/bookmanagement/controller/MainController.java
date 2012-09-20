package com.cec.intelpress.bookmanagement.controller;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Handles and retrieves person request
 */
@Controller
@RequestMapping("/")
public class MainController {

	protected static Logger logger = Logger.getLogger("controller");

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String getMain(Model model) {
		return "index";
	}

}
