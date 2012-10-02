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
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.Role;
import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.RoleService;
import com.cec.intelpress.bookmanagement.service.UserService;

@Controller
@SessionAttributes
@RequestMapping("/admin/rolemanagement")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class RoleManagementController {

	protected static Logger logger = Logger
			.getLogger("RoleManagementController");

	@Resource(name = "UserService")
	private UserService userService;
	@Resource(name = "RoleService")
	private RoleService roleService;

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getRoleManagement(Model model) {

		ModelAndView mav = new ModelAndView();

		List<Role> allRoles = roleService.getAll();
		List<User> allUsers = userService.getAll();
		
		mav.addObject("roles", allRoles);
		mav.addObject("users", allUsers);
		mav.setViewName("rolemanagement");
		return mav;
	}
	
	
	@RequestMapping(value = "/addroletouser", method = RequestMethod.POST)
	public String addRoleToUser(@RequestParam("username")String username, @RequestParam("role")String role) {
		
		User user = userService.getUserByUserName(username);
		if(user != null)
		{
			user.getUserRoles().add(roleService.getByAuthority(role));
			userService.edit(user);
		}
		
		return "redirect:/admin/rolemanagement/";
	}
	
	@RequestMapping(value = "/delrolefromuser/{roleid}/{userid}", method = RequestMethod.GET)
	public String deleteRoleFromUser(@PathVariable(value = "roleid") int roleId,
			@PathVariable(value = "userid") int userId) {
		
		User user = userService.get(userId);
		Role role = roleService.get(roleId);
		user.deleteRole(role);
		
		userService.edit(user);
		return "redirect:/admin/rolemanagement/";
	}

	@RequestMapping(value = "/createrole", method = RequestMethod.POST)
	public String createRole(@ModelAttribute("role") Role role,
			BindingResult result) {
		
		roleService.add(role);
		return "redirect:/admin/rolemanagement/";
	}
}
