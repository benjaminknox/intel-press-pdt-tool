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
package com.cec.intelpress.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.apache.commons.lang3.StringUtils;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.criterion.Order;
import org.hibernate.criterion.Projections;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.Assert;

import com.cec.intelpress.model.AbstractAuditableEntity;
import com.cec.intelpress.model.AbstractEntity;

/**
 * Base Data Access Object for other daos to extend from
 *
 * @author joe.rawlings
 * 
 * @param <E extends AbstractEntity> The entity class for the Dao
 */
public abstract class AbstractDao<E extends AbstractEntity> {

    private static Logger log = LoggerFactory.getLogger(AbstractDao.class);

    @PersistenceContext
    private EntityManager entityManager;

    private Class<E> entityClass;

    /**
     * Constructs a new AbstractDao
     * 
     * @param entityClass
     */
    protected AbstractDao(Class<E> entityClass) {
        super();
        Assert.notNull(entityClass, "entityClass == null");
        this.entityClass = entityClass;
    }

    /**
     * @return The entityClass
     */
    public Class<E> getEntityClass() {
        return entityClass;
    }

    /**
     * Constructs a new instance of the entity class
     * 
     * @return
     */
    public E newEntityInstance() {
        try {
            return entityClass.newInstance();
        } catch (InstantiationException e) {
            log.error(String.format("Exception while creating new instance of %s", entityClass.getSimpleName()), e);
            throw new RuntimeException(String.format("Exception while creating new instance of %s", entityClass.getSimpleName()), e);
        } catch (IllegalAccessException e) {
            log.error(String.format("Access Exception while creating new instance of %s", entityClass.getSimpleName()), e);
            throw new RuntimeException(String.format("Access Exception while creating new instance of %s", entityClass.getSimpleName()), e);
        }
    }

    /**
     * Performs flush of the entity manager
     */
    @Transactional
    public void flush() {
        getEntityManager().flush();
    }

    /**
     * Obtain a lazy-loading reference to the Entity without quering the
     * database. Until the first getter/setters are called
     * 
     * @param id
     * @return
     * @see javax.persistence.EntityManager#getReference(java.lang.Class,
     *      java.lang.Object)
     */
    @Transactional
    public E getReference(long id) {
        return getEntityManager().getReference(entityClass, Long.valueOf(id));
    }

    /**
     * @param id
     * @return
     * @see javax.persistence.EntityManager#find(java.lang.Class,
     *      java.lang.Object)
     */
    @Transactional
    public E find(long id) {
        return getEntityManager().find(entityClass, Long.valueOf(id));
    }

    /**
     * Merges a domain class instance back into the current persistent context
     * and returns a new merged instance.
     * 
     * @param entity
     * @return
     * @see javax.persistence.EntityManager#merge(java.lang.Object)
     */
    @Transactional
    public E merge(E entity) {
        return getEntityManager().merge(entity);
    }

    /**
     * Saves a domain class instance to the database cascading updates to any
     * child instances if required.
     * 
     * @param entity
     * @see javax.persistence.EntityManager#persist(java.lang.Object)
     */
    @Transactional
    public void persist(E entity) {
        getEntityManager().persist(entity);
    }

    /**
     * Refreshes a domain classes state from the database
     * 
     * @param entity
     * @see javax.persistence.EntityManager#refresh(java.lang.Object)
     */
    @Transactional
    public void refresh(E entity) {
        getEntityManager().refresh(entity);
    }

    /**
     * Indicates that a persistent instance should be deleted.
     * 
     * @param entity
     * @see javax.persistence.EntityManager#remove(java.lang.Object)
     */
    @Transactional
    public void remove(long id) {
        E entity = getReference(id);
        if (entity != null) {
            getEntityManager().remove(entity);
        }
    }

    /**
     * Indicates that a persistent instance should be deleted.
     * 
     * @param entity
     * @see javax.persistence.EntityManager#remove(java.lang.Object)
     */
    @Transactional
    public void remove(E entity) {
        if (entity != null) {
            getEntityManager().remove(entity);
        }
    }

    /**
     * Create a new <tt>Criteria</tt> instance, for the given entity class, or a
     * superclass of an entity class.
     * 
     * @return Criteria
     */
    @Transactional
    public Criteria createCriteria() {
        Session session = getSession();
        return session.createCriteria(entityClass);
    }

    /**
     * Counts the number of instances in the database and returns the result
     * 
     * @return number of instances in the database
     */
    @Transactional
    public long count() {
        Long count = (Long) createCriteria().setProjection(Projections.rowCount()).uniqueResult();

        if (count == null) {
            return 0;
        }
        return count.longValue();
    }

    /**
     * Obtains a full list of all instances in the database. Limits the list
     * based on firstResult + maxResult
     */
    @Transactional
    public List<E> findAll(int firstResult, int maxResults) {
        return findAll(firstResult, maxResults, null, true);
    }

    /**
     * Obtains a full list of all instances in the database.  Limits the list
     * based on firstResult + maxResult, sorted by a field and ordering
     */
    @Transactional
    @SuppressWarnings("unchecked")
    public List<E> findAll(int firstResult, int maxResults, String ordering, boolean ascending) {
        Criteria c = createCriteria();
        orderCriteria(c, ordering, ascending);
        return c.setFirstResult(firstResult).setMaxResults(maxResults).list();
    }

    /**
     * Obtains a full list of all instances in the database.
     */
    @Transactional
    public List<E> findAll() {
        return findAll(null, true);
    }

    /**
     * Obtains a full list of all instances in the database, sorted by a field and ordering.
     */
    @Transactional
    public List<E> findAll(String ordering) {
        return findAll(ordering, true);
    }

    /**
     * Obtains a full list of all instances in the database, sorted by a field and ordering with direction
     */
    @Transactional
    @SuppressWarnings("unchecked")
    public List<E> findAll(String ordering, boolean ascending) {
        Criteria c = createCriteria();    	
        orderCriteria(c, ordering, ascending);    		
        return (List<E>) c.list();
    }

    /**
     * Sets up the ordering for a Criteria query.  Both ordering and ascending are
     * actually optional, if ordering is blank nothing will happen to the Criteria.
     * If ascending is blank the direction is assumed to be descending, but generally
     * functions just input true as a default.
     * 
     * @param c
     * 			Criteria you want to order
     * @param ordering
     * 			field to order on
     * @param ascending
     * 			direction to order on
     */
    protected void orderCriteria(Criteria c, String ordering, boolean ascending) {
        // Don't try to order anything unless we have an ordering.
        if (!StringUtils.isBlank(ordering)) {
            try {
                // We need to check that the field is legit for this class.
                // This will either succeed and go through with ordering, or it will
                // throw a NoSuchFieldException and the ordering won't happen.    		
                entityClass.getDeclaredField(ordering);

                if (ascending == true) {
                    c.addOrder( Order.asc(ordering) );    		
                } 
                else {
                    c.addOrder( Order.desc(ordering) );
                }
            }
            catch (NoSuchFieldException nsfe) {
                // We don't actually care, we just won't order it.		
                log.warn("Tried to order {} using invalid field {} with ascending {}", 
                        new Object[] { entityClass, ordering, ascending });				
            }
        }

        return;
    }

    /**
     * Obtains a reference to the JPA EntityManager
     * 
     * @return The entityManager
     */
    protected EntityManager getEntityManager() {
        if (entityManager == null) {
            throw new IllegalStateException("Entity manager has not been injected (is the Spring Aspects JAR configured as an AJC/AJDT aspects library?)");
        }
        return entityManager;
    }

    /**
     * Obtain a reference to the Hibernate Session
     * 
     * @return
     */
    protected Session getSession() {
        Object session = getEntityManager().getDelegate();
        if (session == null || !(session instanceof Session)) {
            throw new IllegalStateException("EntityManager is not an implementation of Hibernate 3.5 or above");
        }
        return (Session) session;
    }
}
