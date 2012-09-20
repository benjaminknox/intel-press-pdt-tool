package com.cec.intelpress.bookmanagement.service;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.UserRole;

@Service("UserRoleService")
@Transactional
public class UserRoleService {

	protected static Logger logger = Logger.getLogger("UserRoleService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<UserRole> getAll() {
		logger.debug("Retrieving all persons");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  UserRole");

		return query.list();
	}

	public UserRole get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		UserRole userRole = (UserRole) session.get(UserRole.class, id);

		return userRole;
	}

	public void add(UserRole userRole) {
		logger.debug("Adding new user");

		Session session = sessionFactory.getCurrentSession();

		session.save(userRole);
	}

	public void delete(Integer id) {
		logger.debug("Deleting existing user");

		Session session = sessionFactory.getCurrentSession();

		UserRole userRole = (UserRole) session.get(UserRole.class, id);

		session.delete(userRole);
	}

	public void edit(UserRole userRole) {
		logger.debug("Editing existing person");

		Session session = sessionFactory.getCurrentSession();

		UserRole existingUserRole = (UserRole) session.get(UserRole.class, userRole.getId());

		existingUserRole.setAuthority(userRole.getAuthority());
		existingUserRole.setUser_id(userRole.getUser_id());

		session.save(userRole);
	}
}