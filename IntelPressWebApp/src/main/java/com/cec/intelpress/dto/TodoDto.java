/*
 * Copyright (c) 2012 Cummings Engineering Consultants.  All Rights Reserved.
 *
 * This software is proprietary to, and a valuable trade secret of, Cummings
 * Engineering Consultants.
 *
 * The software and documentation may not be copied, reproduced, translated,
 * or reduced to any electronic medium or machine-readable form without a
 * prior written agreement from Cummings Engineering Consultants.
 *
 *
 * UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, THE SOFTWARE
 * AND DOCUMENTATION ARE DISTRIBUTED ON AN "AS IS" BASIS, WITHOUT WARRANTIES
 * OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 * PURPOSE AND NONINFRINGEMENT.  REFER TO THE WRITTEN AGREEMENT FOR SPECIFIC
 * LANGUAGE GOVERNING PERMISSIONS AND LIMITATIONS.
 */
package com.cec.intelpress.dto;

import com.cec.intelpress.model.Todo;

import java.io.Serializable;

import javax.validation.constraints.NotNull;

/**
 * Abstract Data Transfer Object with some default attributes
 * 
 * @author joe.rawlings
 */
public class TodoDto extends AbstractDto {

	private static final long serialVersionUID = -1308795024262635690L;

	@NotNull
	private String title;

	private boolean completed = false;

	private int order;

	public TodoDto() {
	}

	public TodoDto(Todo todo) {
		super(todo.getId());
		this.title = todo.getTitle();
		this.order = todo.getPosition();
		this.completed = todo.isCompleted();
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public int getOrder() {
		return order;
	}

	public void setOrder(int order) {
		this.order = order;
	}

	public boolean isCompleted() {
		return completed;
	}

	public void setCompleted(boolean completed) {
		this.completed = completed;
	}

	@Override
	public String toString() {
		return super.toString() + " title = " + title + ", completed = " + completed + ", id = " + this.getId();
	}

}
