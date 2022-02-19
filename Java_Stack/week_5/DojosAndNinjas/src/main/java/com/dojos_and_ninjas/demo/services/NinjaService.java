package com.dojos_and_ninjas.demo.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.dojos_and_ninjas.demo.models.Dojo;
import com.dojos_and_ninjas.demo.models.Ninja;
import com.dojos_and_ninjas.demo.repositories.NinjaRepository;

@Service
public class NinjaService {
	
	@Autowired
	private NinjaRepository repo;
	
	@Autowired
	private DojoService dojoService;

    // CREATE
    // create a ninja and link to a dojo 
    public Ninja create(Ninja ninja) {
        return this.repo.save(ninja);   // with or without this, same result
    }
    
    // READ
    // return all ninjas
    public List<Ninja> getAll() {
        return repo.findAll();
    }  
    
    // return a ninja by id
    public Ninja retrieve(Long ninjaId) {
    	return this.repo.findById(ninjaId).get();
    }
    
    // UPDATE
    // update a ninja by id
    public Ninja update(Ninja ninjaId) {
    	return this.repo.save(ninjaId);
    }
    
    // DELETE
    // delete a ninja by id
    public void delete(Long ninjaId) {
    	this.repo.deleteById(ninjaId);
    }
    
}