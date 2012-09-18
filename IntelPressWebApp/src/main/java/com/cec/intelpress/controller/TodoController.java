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
package com.cec.intelpress.controller;

import com.cec.intelpress.dao.TodoDao;
import com.cec.intelpress.model.Todo;
import com.cec.intelpress.dto.TodoDto;

import java.util.List;
import java.util.ArrayList;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import javax.validation.Valid;

/**
 * Controller for the Todo model
 *
 * @author joe.rawlings
 */
@Controller
@RequestMapping("/todo")
public class TodoController {
	
	private static final Logger logger = LoggerFactory.getLogger(TodoController.class);

	@Autowired
	private TodoDao todoDao;
	
	@RequestMapping(method = RequestMethod.GET, consumes = "application/json", produces = "application/json")
	public ResponseEntity<List<TodoDto>> list() {
		logger.info("Received request to list todos");
		List<Todo> todos = todoDao.findAll();
		logger.info("Todo Listing count = " + todos.size());

		List<TodoDto> dtos = new ArrayList<TodoDto>();

		if(todos != null) {
			for(Todo todo : todos) {
				dtos.add(new TodoDto(todo));
			}
		}
		return new ResponseEntity<List<TodoDto>>(dtos, HttpStatus.OK);
	}

	@RequestMapping(value = "/{id}", method = RequestMethod.GET)
	public ResponseEntity<TodoDto> get(@PathVariable("id") long id) {		
		logger.debug("Received request to lookup Todo id : " + id);

		ResponseEntity<TodoDto> response = null;

		Todo todo = todoDao.find(id);
		if(todo != null) {
			response = new ResponseEntity<TodoDto>(new TodoDto(todo), HttpStatus.OK);
		}

 		if(response == null) {
 			response = new ResponseEntity(null, HttpStatus.NOT_FOUND);
 		}
 		
		return response;
	}
	
	@RequestMapping(method = RequestMethod.POST) 
	public ResponseEntity create(@RequestBody @Valid TodoDto todoDto) {
		logger.debug("Save todo " + todoDto);

		Todo todo = new Todo();
		todo.setTitle(todoDto.getTitle());
		todo.setPosition(todoDto.getOrder());
		todo.setCompleted(todoDto.isCompleted());
		todoDao.persist(todo);
		return new ResponseEntity(new TodoDto(todo), HttpStatus.CREATED);
	}

	@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
	public ResponseEntity<TodoDto> update(@PathVariable("id") long id, final @RequestBody @Valid TodoDto todoDto) {		
		logger.debug("Received request to update Todo id : " + id);

		ResponseEntity<TodoDto> response = null;

		Todo todo = todoDao.find(id);
		if(todo != null) {
			todo.setTitle(todoDto.getTitle());
			todo.setCompleted(todoDto.isCompleted());
			todo.setPosition(todoDto.getOrder());
			todoDao.merge(todo);
			response = new ResponseEntity<TodoDto>(new TodoDto(todo), HttpStatus.OK);
		}

 		if(response == null) {
 			response = new ResponseEntity(null, HttpStatus.NOT_FOUND);
 		}
 		
		return response;
	}

	@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
	public ResponseEntity<TodoDto> delete(@PathVariable("id") long id) {		
		logger.debug("Received request to delete Todo id : " + id);

		ResponseEntity<TodoDto> response = null;

		Todo todo = todoDao.find(id);
		if(todo != null) {
			todoDao.remove(id);
			response = new ResponseEntity(null, HttpStatus.NO_CONTENT);
		}

 		if(response == null) {
 			response = new ResponseEntity(null, HttpStatus.NOT_FOUND);
 		}
 		
		return response;
	}
}
