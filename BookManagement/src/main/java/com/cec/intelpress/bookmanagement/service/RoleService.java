package com.cec.intelpress.bookmanagement.service;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.Role;

@Service("RoleService")
@Transactional
public class RoleService {

	protected static Logger logger = Logger.getLogger("UserRoleService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<Role> getAll() {
		logger.debug("Retrieving all persons");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  Role");

		return query.list();
	}

	public Role get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		Role role = (Role) session.get(Role.class, id);

		return role;
	}

	public Role getByAuthority(String authority)
	{
		Session session = sessionFactory.getCurrentSession();
		
		for(Role role: getAll())
		{
			if(role.getAuthority().equals(authority))
			{
				return role;
			}
		}
		
		return null;
	}
	public void add(Role role) {
		logger.debug("Adding new user");

		Session session = sessionFactory.getCurrentSession();
		session.save(role);
		session.flush();

	}

	public void delete(Integer id) {
		logger.debug("Deleting existing user");

		Session session = sessionFactory.getCurrentSession();

		Role role = (Role) session.get(Role.class, id);

		session.delete(role);
		session.flush();

	}

	public void edit(Role role) {
		logger.debug("Editing existing person");

		Session session = sessionFactory.getCurrentSession();

		Role existingRole = (Role) session.get(Role.class,
				role.getId());

		existingRole.setAuthority(role.getAuthority());

		session.save(role);
		session.flush();

	}
}