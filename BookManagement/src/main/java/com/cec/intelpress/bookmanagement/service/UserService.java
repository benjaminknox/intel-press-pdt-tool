package com.cec.intelpress.bookmanagement.service;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.User;

@Service("UserService")
@Transactional
public class UserService {

	protected static Logger logger = Logger.getLogger("UserService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<User> getAll() {
		logger.debug("Retrieving all persons");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  User");

		return query.list();
	}

	public User get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		User user = (User) session.get(User.class, id);

		return user;
	}

	public void add(User user) {
		logger.debug("Adding new user");

		Session session = sessionFactory.getCurrentSession();

		session.save(user);
	}

	public void delete(Integer id) {
		logger.debug("Deleting existing user");

		Session session = sessionFactory.getCurrentSession();

		User user = (User) session.get(User.class, id);

		session.delete(user);
	}

	public void edit(User user) {
		logger.debug("Editing existing person");

		Session session = sessionFactory.getCurrentSession();

		User existingPerson = (User) session.get(User.class, user.getId());

		existingPerson.setUsername(user.getUsername());
		existingPerson.setPassword(user.getPassword());

		session.save(user);
	}
}