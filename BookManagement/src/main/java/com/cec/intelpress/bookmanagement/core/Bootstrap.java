package com.cec.intelpress.bookmanagement.core;

import javax.annotation.Resource;

import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;

import com.cec.intelpress.bookmanagement.domain.Role;
import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.RoleService;
import com.cec.intelpress.bookmanagement.service.UserService;
import com.cec.intelpress.bookmanagement.util.Util;

@Component
public class Bootstrap implements ApplicationListener<ContextRefreshedEvent> {

	private String firstname = "Admin";
	private String lastname = "Admin";
	private String email = "admin@admin.com";
	private String username = "admin";
	private String password = "dongs";

	@Resource(name="UserService")
	private UserService userService;
	@Resource(name="RoleService")
	private RoleService roleService;

	public void onApplicationEvent(ContextRefreshedEvent event) {
		
		if(!(userService.getAll().size() > 0))
		{
			User user = new User();
			user.setUsername(username);
			user.setFirstname(firstname);
			user.setLastname(lastname);
			user.setEmail(email);
			user.setPassword(Util.sha256HashString(password));
			user.setEnabled(1);
			
			Role userRole = new Role();
			userRole.setAuthority("ROLE_USER");
			
			Role adminRole = new Role();
			adminRole.setAuthority("ROLE_ADMIN");
			
			user.getUserRoles().add(userRole);
			user.getUserRoles().add(adminRole);
			
			roleService.add(userRole);
			roleService.add(adminRole);	
			userService.add(user);			
		}
	}
}
