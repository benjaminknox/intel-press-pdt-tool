package com.cec.intelpress.bookmanagement.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cec.intelpress.bookmanagement.domain.Book;
import com.cec.intelpress.bookmanagement.domain.Chapter;

@Service("BookService")
@Transactional
public class BookService {

	protected static Logger logger = Logger.getLogger("BookService");

	@Resource(name = "sessionFactory")
	private SessionFactory sessionFactory;
	
	@Resource(name = "ChapterService")
	private ChapterService chapterService;
	
	@Resource(name = "PdfBookService")
	private PdfBookService pdfService;
	
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
				suggestedBookList.add(book);
		}
		
		return suggestedBookList;
	}

	public Book get(String id) {
		Session session = sessionFactory.getCurrentSession();

		Book book = (Book) session.get(Book.class, id);

		return book;
	}

	public void add(Book book) {
		logger.debug("Adding new book");
		Session session = sessionFactory.getCurrentSession();
		session.save(book);
	}

	public void delete(String id) {
		logger.debug("Deleting existing book");

		Session session = sessionFactory.getCurrentSession();

		Book book = (Book) session.get(Book.class, id);
		Set<Chapter> chapters = book.getBookChapters();
		//Have to remove all of the chapters before we can kill the book
		for (Chapter chapter : chapters) {
			chapterService.delete(chapter.getId());
		}
		session.delete(book);
	}

	/**
	 * Updates the books information from the java object
	 * @param book the new book 
	 */
	public void edit(Book book) {
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
		existingBook.setTitle(book.getTitle());
		existingBook.setBookcovername(book.getBookcovername());
		session.merge(existingBook);
	}
	
	/**
	 * This updates the book attached to the old ID with the content of the Book object passed in.
	 * @param book new content
	 * @param oldBookId old database object
	 */
	public void edit(Book book, String oldBookId) {
		Session session = sessionFactory.getCurrentSession();

		Book existingBook = (Book) session.get(Book.class, oldBookId);
		
		existingBook.setAuthor(book.getAuthor());
		existingBook.setBookChapters(existingBook.getBookChapters());
		existingBook.setBookcover(book.getBookcover());
		existingBook.setBuyurl(book.getBuyurl());
		existingBook.setCategory(book.getCategory());
		existingBook.setDescription(book.getDescription());
		existingBook.setIsbn(book.getIsbn());
		existingBook.setPublisher(book.getPublisher());
		existingBook.setTitle(book.getTitle());
		if (book.getBookcovername() != null) {
			existingBook.setBookcovername(book.getBookcovername());
		} else {
			existingBook.setBookcovername(existingBook.getBookcovername());
		}
		session.merge(existingBook);
	}
}