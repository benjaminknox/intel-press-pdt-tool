package com.cec.intelpress.bookmanagement.service;

import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.Chapter;

@Service("ChapterService")
@Transactional
public class ChapterService {

	protected static Logger logger = Logger.getLogger("ChapterService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<Chapter> getAll() {
		logger.debug("Retrieving all persons");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  Chapter");

		return query.list();
	}

	public Chapter get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		Chapter chapter = (Chapter) session.get(Chapter.class, id);

		return chapter;
	}

	public void add(Chapter chapter) {
		logger.debug("Adding new chapter");
		Session session = sessionFactory.getCurrentSession();
		session.save(chapter);
	}

	public void delete(Integer id) {
		logger.debug("Deleting existing chapter");

		Session session = sessionFactory.getCurrentSession();

		Chapter chapter = (Chapter) session.get(Chapter.class, id);
		session.delete(chapter);
	}

	public void edit(Chapter chapter) {
		logger.debug("Editing existing chapter");

		Session session = sessionFactory.getCurrentSession();

		Chapter existingChapter = (Chapter) session.get(Chapter.class, chapter.getId());
		existingChapter.setChapterNumber(chapter.getChapterNumber());
		existingChapter.setCompleted(chapter.getCompleted());
		existingChapter.setInprogress(chapter.getInprogress());
		existingChapter.setName(chapter.getName());
		existingChapter.setWorkedOnBy(chapter.getWorkedOnBy());
		existingChapter.setArticle(chapter.getArticle());
		existingChapter.setAssignedUser(chapter.getAssignedUser());
		session.merge(existingChapter);
	}
	
	public List<Chapter> getAllWithoutArticles() {
		logger.debug("Grabbing all chapters without articles");
		
		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  Chapter chapter where chapter.technical = true and chapter.article = NULL");

		return query.list();
	}
}