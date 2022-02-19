package com.dojos_and_ninjas.demo.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.dojos_and_ninjas.demo.models.Dojo;
import com.dojos_and_ninjas.demo.models.Ninja;

@Repository
public interface NinjaRepository extends CrudRepository<Ninja, Long> {

	List<Ninja> findAll();
	List<Ninja> findAllByDojo(Dojo dojo);
}