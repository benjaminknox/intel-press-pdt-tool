package com.cec.intelpress.bookmanagement.service;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.TechnicalArticle;

/**
 * This service deals and acts as a DAO for Technical Articles
 * @author prius
 *
 */
@Service("ArticleService")
@Transactional
public class ArticleService {

	protected static Logger logger = Logger.getLogger("articleService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<TechnicalArticle> getAll() {
		logger.debug("Retrieving all articles");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  TechnicalArticle");

		return query.list();
	}
	
	public TechnicalArticle get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		TechnicalArticle article = (TechnicalArticle) session.get(TechnicalArticle.class, id);

		return article;
	}

	public void add(TechnicalArticle article) {
		logger.debug("Adding new TechnicalArticle");
		Session session = sessionFactory.getCurrentSession();
		session.save(article);
	}

	public void delete(Integer id) {
		logger.debug("Deleting existing TechnicalArticle");

		Session session = sessionFactory.getCurrentSession();

		TechnicalArticle article = (TechnicalArticle) session.get(TechnicalArticle.class, id);
		session.delete(article);
	}

	public void edit(TechnicalArticle article) {
		logger.debug("Editing existing TechnicalArticle");

		Session session = sessionFactory.getCurrentSession();

		TechnicalArticle existingarticle = (TechnicalArticle) session.get(TechnicalArticle.class, article.getId());
		existingarticle.setArticle(article.getArticle());
		existingarticle.setAuthor(article.getAuthor());
		existingarticle.setCompleted(article.isCompleted());
		existingarticle.setTitle(article.getTitle());
		session.merge(existingarticle);
	}

}