package com.save_travels.demo.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.save_travels.demo.models.Expense;
import com.save_travels.demo.repositories.ExpenseRepository;

@Service
public class ExpenseService {
	
	@Autowired
	private ExpenseRepository repo;

	public List<Expense>all(){
		return this.repo.findAll();
	}
	
	public Expense create(Expense item) {
		return this.repo.save(item);
	}
	
	public Expense retrieve(Long itemId) {
		return this.repo.findById(itemId).get();
	}
	
	public void delete(Long itemId) {
		this.repo.deleteById(itemId);
	}
	
	
}
