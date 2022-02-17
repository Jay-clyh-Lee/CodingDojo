package com.save_travels.demo.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.save_travels.demo.models.Expense;
import com.save_travels.demo.services.ExpenseService;


@Controller
public class ExpenseController {

	@Autowired
	private ExpenseService expenseService;
	
	@GetMapping("/")
	public String home() {
		return "home.jsp";
	}
	
	// CREATE
//	// create page
//	@GetMapping("/expense/new")
//	public String home(@ModelAttribute("expenses") Expense anExpenseObject) {
//		return "home.jsp";
//	}
	
	// create form
	@PostMapping("/expense/create")
	public String createExpense(
			@Valid @ModelAttribute("expenses") Expense anExpenseObject,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if (result.hasErrors()) return "home.jsp";
		
		this.expenseService.create(anExpenseObject);
		
		redirectAttributes.addFlashAttribute("message", "A new expense has been added.");
		
		return "redirect:/home";
	}
	
	// VIEW
	@GetMapping("/expense/view/{id}")
	public String viewExpense(
			@PathVariable Long id,
			@ModelAttribute("expenses") Expense anExpenseObject
			) {
		
		this.expenseService.retrieve(id);
		
		return "viewExpense.jsp";
	}
	
	// EDIT
	// edit page
	@GetMapping("/expense/edit/{id}")
	public String editExpense(@ModelAttribute("expenses") Expense anExpenseObject) {
		return "editExpense.jsp";
	}
	// edit form
	@PostMapping("/expense/update/{id}")
	public String updateExpense(
			@Valid @ModelAttribute("expenses") Expense anExpenseObject,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if (result.hasErrors()) return "home.jsp";
		
		this.expenseService.create(anExpenseObject);
		
		redirectAttributes.addFlashAttribute("message", "A new expense has been added.");
		
		return "redirect:/expense/view/{id}";
	}
	
}
