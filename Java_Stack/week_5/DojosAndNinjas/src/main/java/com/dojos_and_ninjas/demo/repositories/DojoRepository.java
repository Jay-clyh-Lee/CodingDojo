package com.dojos_and_ninjas.demo.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.dojos_and_ninjas.demo.models.Dojo;

@Repository
public interface DojoRepository extends CrudRepository<Dojo, Long> {

	List<Dojo> findAll();
}