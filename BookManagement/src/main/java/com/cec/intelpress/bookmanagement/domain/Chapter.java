package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "chapters")
public class Chapter implements Serializable, Comparable<Chapter> {

	private static final long serialVersionUID = -5527566243002296042L;

	@Id
	@Column(name = "chapter_id")
	@GeneratedValue
	private Integer id;

	@Column(name = "name")
	private String name;

	@Column(name = "chapternumber")
	private Integer chapterNumber;

	@Column(name = "completed")
	private Boolean completed;

	@Column(name = "inprogress")
	private Boolean inprogress;

	@Column(name = "workedonby")
	private String workedOnBy;

	@Column(name = "technical")
	private boolean technical;
	
	@ManyToOne
	@JoinColumn (name="book_id")
	private Book book;

	@OneToOne(cascade = CascadeType.ALL)
	private TechnicalArticle article;
	
	@OneToOne(cascade = CascadeType.ALL)
	private User assignedUser;

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Integer getChapterNumber() {
		return chapterNumber;
	}

	public void setChapterNumber(Integer chapterNumber) {
		this.chapterNumber = chapterNumber;
	}

	public Boolean getCompleted() {
		return completed;
	}

	public void setCompleted(Boolean completed) {
		this.completed = completed;
	}

	public Boolean getInprogress() {
		return inprogress;
	}

	public void setInprogress(Boolean inprogress) {
		this.inprogress = inprogress;
	}

	public String getWorkedOnBy() {
		return workedOnBy;
	}

	public void setWorkedOnBy(String workedOnBy) {
		this.workedOnBy = workedOnBy;
	}

	public boolean isTechnical() {
		return technical;
	}

	public void setTechnical(boolean technical) {
		this.technical = technical;
	}

	public TechnicalArticle getArticle() {
		return article;
	}

	public void setArticle(TechnicalArticle article) {
		this.article = article;
	}

	public Book getBook() {
		return book;
	}

	public void setBook(Book book) {
		this.book = book;
	}

	public int compareTo(Chapter o) {
		return this.chapterNumber;
	}

	public User getAssignedUser() {
		return assignedUser;
	}

	public void setAssignedUser(User assignedUser) {
		this.assignedUser = assignedUser;
	}

}