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

@Service("BookService")
@Transactional
public class BookService {

	protected static Logger logger = Logger.getLogger("BookService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;

	public List<Book> getAll() {
		logger.debug("Retrieving all persons");

		Session session = sessionFactory.getCurrentSession();

		Query query = session.createQuery("FROM  Book");

		return query.list();
	}
	
	public List<Book> getAllSuggested() {
		logger.debug("Retrieving all persons");
		List<Book> suggestedBookList = new ArrayList<Book>();
		Session session = sessionFactory.getCurrentSession();
		Query query = session.createQuery("FROM  Book");
		
		for(Book book : (List<Book>)query.list())
		{
			if(book.getSuggestedReading() == true)
			{
				suggestedBookList.add(book);
			}
		}
		
		return suggestedBookList;
	}

	public Book get(Integer id) {
		Session session = sessionFactory.getCurrentSession();

		Book book = (Book) session.get(Book.class, id);

		return book;
	}

	public void add(Book book) {
		logger.debug("Adding new book");
		Session session = sessionFactory.getCurrentSession();
		session.save(book);
	}

	public void delete(Integer id) {
		logger.debug("Deleting existing book");

		Session session = sessionFactory.getCurrentSession();

		Book book = (Book) session.get(Book.class, id);
		book.getBookChapters().clear();
		session.delete(book);
	}

	public void edit(Book book) {
		logger.debug("Editing existing person");

		Session session = sessionFactory.getCurrentSession();

		Book existingBook = (Book) session.get(Book.class, book.getId());
		existingBook.setAuthor(book.getAuthor());
		existingBook.setBookChapters(book.getBookChapters());
		existingBook.setBookcover(book.getBookcover());
		existingBook.setBuyurl(book.getBuyurl());
		existingBook.setCategory(book.getCategory());
		existingBook.setDescription(book.getDescription());
		existingBook.setIsbn(book.getIsbn());
		existingBook.setPublisher(book.getPublisher());
		existingBook.setSuggestedReading(book.getSuggestedReading());
		existingBook.setTitle(book.getTitle());
		session.merge(existingBook);
	}
}