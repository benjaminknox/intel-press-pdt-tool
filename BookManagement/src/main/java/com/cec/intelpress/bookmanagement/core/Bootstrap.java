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
			user.setPassword(Util.sha256HashString(password));
			user.setEnabled(1);
			
			Role role = new Role();
			role.setAuthority("ROLE_ADMIN");
			
			user.getUserRoles().add(role);
			
			roleService.add(role);	
			userService.add(user);			
		}
	}
}
