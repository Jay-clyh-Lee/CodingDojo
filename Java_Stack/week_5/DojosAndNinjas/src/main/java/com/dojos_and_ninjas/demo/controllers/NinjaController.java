package com.dojos_and_ninjas.demo.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.dojos_and_ninjas.demo.models.Dojo;
import com.dojos_and_ninjas.demo.models.Ninja;
import com.dojos_and_ninjas.demo.services.DojoService;
import com.dojos_and_ninjas.demo.services.NinjaService;

@Controller
public class NinjaController {
	
	@Autowired
	private NinjaService ninjaService;

	@Autowired
	private DojoService dojoService;
	// READ
	// view all ninjas
	@GetMapping("/ninjas")
	public String viewAllNinjas(Model model) {
		
		model.addAttribute("ninja", this.ninjaService.getAll());
		return "ninjas.jsp"; // view all ninjas page
	}
	
	// view a ninja by id
	@GetMapping("/ninja/view/{id}")
	public String viewNinjaById(
			@PathVariable Long id,
			Model model
			) {
		
		model.addAttribute("ninja", this.ninjaService.retrieve(id));
		
		return "viewNinja.jsp";
	}
	
	// CREATE
	// add dojo page
	@GetMapping("/ninja/add")
	public String add(@ModelAttribute("ninja") Ninja ninja, Model model) {
		
		model.addAttribute("dojos", this.dojoService.getAll());
		return "newNinja.jsp";
	}
	
	@PostMapping("/ninja/create")
	public String create(
			@Valid @ModelAttribute("ninja") Ninja ninja,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if ( !result.hasErrors() ) {
			
			ninja = this.ninjaService.create(ninja);
			
			if ( ninja == null ) return "redirect:/ninja/add";
			
			redirectAttributes.addFlashAttribute("message", "Your ninja has been Added");
		}		
		return "redirect:/dojos";
	}
		
	// UPDATE
	// edit a dojo page
	@GetMapping("/ninja/edit/{id}")
	public String editDojoByIdFormPage(
			@PathVariable Long id,
			Model model
			) {
			
		model.addAttribute("ninja", this.ninjaService.retrieve(id));
		
		return "editNinja.jsp";
	}
		
	@PostMapping("/ninja/update/{id}")
	public String update(  // what if this has the same name in NinjaService.java
			@Valid @ModelAttribute("ninja") Ninja ninja,
			BindingResult result,
			RedirectAttributes redirectAttributes
				) {
			
		if ( result.hasErrors() ) return "editNinja.jsp";
		
		this.ninjaService.update(ninja); 
		
		redirectAttributes.addFlashAttribute("message", "This ninja has been updated");
		
		return String.format("redirect:/ninja/%d", ninja.getId()); // view the updated ninja
	}
		
	//DELETE
	@GetMapping("/ninja/delete/{id}")
	public String delete(
			@PathVariable Long id,
			RedirectAttributes redirectAttributes
			) {
			
		this.ninjaService.delete(id);
			
		redirectAttributes.addFlashAttribute("message", "This ninja has been deleted");
			
		return "redirect:/";
	}
	
}
