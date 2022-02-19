package com.dojos_and_ninjas.demo.services;

import java.util.List;
//import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.dojos_and_ninjas.demo.models.Dojo;
import com.dojos_and_ninjas.demo.repositories.DojoRepository;

@Service
public class DojoService {
	
	@Autowired
	private DojoRepository repo;

    public Dojo create(Dojo item) {
        return this.repo.save(item);
    }
    
	// READ
    // return all dojos
    public List<Dojo> getAll() {
        return repo.findAll();
    }

    // return dojo by id
    public Dojo retrieve(Long itemId) {
    	return this.repo.findById(itemId).get();
    }

    // UPDATE
    // update a dojo by id
	public Dojo update(Dojo item) {
		return this.repo.save(item);
	}
	
	// DELETE
	// delete a dojo by id
	public void delete(Long itemId) {
		this.repo.deleteById(itemId);
	}

}