package com.cec.intelpress.bookmanagement.service;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.PdfBook;
import com.cec.intelpress.bookmanagement.domain.User;

@Service("PdfBookService")
@Transactional
public class PdfBookService {

	protected static Logger logger = Logger.getLogger("PdfBookService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<PdfBook> getAll() {
		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  PdfBook");

		return query.list();
	}
	
	public List<PdfBook> getAllSuggested() {
		List<PdfBook> suggestedBookList = new ArrayList<PdfBook>();
		Session session = sessionFactory.getCurrentSession();
		Query query = session.createQuery("FROM  PdfBook");
		
		for(PdfBook book : (List<PdfBook>)query.list())
		{
			suggestedBookList.add(book);
		}
		
		return suggestedBookList;
	}
	
	public List<PdfBook> getAllNonCompletedBooksByUser(User user) {
		List<PdfBook> suggestedBookList = new ArrayList<PdfBook>();
		Session session = sessionFactory.getCurrentSession();
		Query query = session.createQuery("FROM  PdfBook b where b.uploader = :user and b.converted = 0");
		query.setParameter("user", user);
		
		for(PdfBook book : (List<PdfBook>)query.list())
		{
			suggestedBookList.add(book);
		}
		
		return suggestedBookList;
	}

	public List<PdfBook> getAllCompletedBooksByUser(User user) {
		List<PdfBook> suggestedBookList = new ArrayList<PdfBook>();
		Session session = sessionFactory.getCurrentSession();
		Query query = session.createQuery("FROM  PdfBook b where b.uploader = :user and b.converted = 1");
		query.setParameter("user", user);
		
		for(PdfBook book : (List<PdfBook>)query.list())
		{
			suggestedBookList.add(book);
		}
		
		return suggestedBookList;
	}
	
	public PdfBook get(String id) {
		Session session = sessionFactory.getCurrentSession();

		PdfBook book = (PdfBook) session.get(PdfBook.class, id);

		return book;
	}

	public void add(PdfBook book) {
		Session session = sessionFactory.getCurrentSession();
		session.save(book);
	}

	public void delete(String pdfid) {
		logger.debug("Deleting existing book");

		Session session = sessionFactory.getCurrentSession();

		PdfBook book = (PdfBook) session.get(PdfBook.class, pdfid);
		session.delete(book);
	}

	public void edit(PdfBook book) {
		logger.debug("Editing existing person");

		Session session = sessionFactory.getCurrentSession();

		PdfBook existingBook = (PdfBook) session.get(PdfBook.class, book.getId());
		existingBook.setAuthor(book.getAuthor());
		existingBook.setIsbn(book.getIsbn());
		existingBook.setTitle(book.getTitle());
		existingBook.setEpubFileName(book.getEpubFileName());
		existingBook.setMobiFileName(book.getMobiFileName());
		existingBook.setPdfFileName(book.getPdfFileName());
		existingBook.setConverted(book.isConverted());
		existingBook.setEmail(book.getEmail());
		existingBook.setUploader(book.getUploader());
		session.merge(existingBook);
	}
}