package com.save_travels.demo.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.save_travels.demo.models.Expense;
import com.save_travels.demo.repositories.ExpenseRepository;


@Service
public class ExpenseService {
	
	@Autowired
	private ExpenseRepository repository;

	public List<Expense>all(){
		return this.repository.findAll();
	}
	
	public Expense create(Expense item) {
		return this.repository.save(item);
	}
	
	public Expense retrieve(Long itemId) {
		return this.repository.findById(itemId).get();
	}
	
	public Expense update(Expense item) {
		return this.repository.save(item);
	}
	
	public void delete(Long itemId) {
		this.repository.deleteById(itemId);
	}
	
	
}
