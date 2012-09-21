package com.cec.intelpress.bookmanagement.controller;

import java.util.List;

import javax.annotation.Resource;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.UserService;

@Controller
@RequestMapping("/")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class UserManagementController {
	
	@Resource(name="UserService")
	private UserService userService;
	
	@RequestMapping(value = "/usermanagement", method = RequestMethod.GET)
	public ModelAndView getUserManagement(Model model) {

		List<User> allUsers = userService.getAll();

		return new ModelAndView("usermanagement", "users", allUsers);
	}
	
	@RequestMapping(value = "/deluser/{id}", method= RequestMethod.GET)
	public String deleteUser(@PathVariable(value="id") int id)
	{
		userService.delete(id);
		
		return "redirect:/usermanagement";
	}

}
