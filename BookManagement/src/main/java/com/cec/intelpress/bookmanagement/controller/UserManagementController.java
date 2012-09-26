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
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Role;
import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.RoleService;
import com.cec.intelpress.bookmanagement.service.UserService;
import com.cec.intelpress.bookmanagement.util.Util;

@Controller
@SessionAttributes
@RequestMapping("/admin/usermanagement")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class UserManagementController {

	protected static Logger logger = Logger
			.getLogger("UserManagmentController");

	@Resource(name = "UserService")
	private UserService userService;
	@Resource(name = "RoleService")
	private RoleService roleService;

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getUserManagement(Model model) {

		ModelAndView mav = new ModelAndView();

		List<User> allUsers = userService.getAll();
		List<Role> allRoles = roleService.getAll();

		mav.addObject("users", allUsers);
		mav.addObject("roles", allRoles);
		mav.setViewName("usermanagement");
		return mav;
	}

	@RequestMapping(value = "/deluser/{id}", method = RequestMethod.GET)
	public String deleteUser(@PathVariable(value = "id") int id) {
		userService.delete(id);

		return "redirect:/admin/usermanagement/";
	}

	@RequestMapping(value = "/adduser", method = RequestMethod.POST)
	public String addUser(@ModelAttribute("user") User user,
			BindingResult result) {

		user.setUsername(user.getFirstname().toLowerCase() + "."
				+ user.getLastname().toLowerCase());

		user.setEnabled(1);
		user.setPassword(Util.sha256HashString(user.getPassword()));
		user.getUserRoles().add(roleService.getByAuthority("ROLE_USER"));
		userService.add(user);

		logger.info("Created new user:" + user.getUsername());
		return "redirect:/admin/usermanagement/";
	}
}
