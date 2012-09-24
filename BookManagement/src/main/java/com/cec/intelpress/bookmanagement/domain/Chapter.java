package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "chapters")
public class Chapter implements Serializable {

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

	@OneToMany(fetch = FetchType.EAGER, mappedBy = "bookChapters")
	private Set<Book> books = new HashSet<Book>(0);
	
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

	public Set<Book> getBooks() {
		return books;
	}

	public void setBooks(Set<Book> books) {
		this.books = books;
	}

}