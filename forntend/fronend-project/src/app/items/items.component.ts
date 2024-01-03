import { Component } from '@angular/core';
import { ItemService } from '../item.service'
import { Router } from '@angular/router';
import { HttpClient, HttpEventType } from '@angular/common/http';
@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})

export class ItemsComponent {
  items: any[] = [];
  filterItems : any[] = []
  takenItems: any[] = [];

  name: any
  admin: any

  selectedItemId: any;
  showDetails: boolean = false;

  constructor(private itemService: ItemService, private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchItems();
    this.fetchTakenItems();
    this.getName()
  }

  fetchItems(): void {
    this.itemService.getItems().subscribe(
      (data: any[]) => {
        this.items = data
          .filter(item => !item.taken)
          .map((item) => ({ ...item, clicked: false }));
          this.filterItems = this.items
      },
      (error) => {
        console.error('Error fetching items:', error);
      }
    );
  }

  fetchTakenItems(): void {
    this.itemService.getTakenItems().subscribe(
      (data: any[]) => {
        this.takenItems = data.map((item) => ({ ...item, clicked: false }));
      },
      (error) => {
        console.error('Error fetching taken items:', error);
      }
    );
  }
  selectedCategory: string | null = null;


  filter(category: any): void {
    this.filterItems = this.items.filter(item => {
      return item.item_category == category.target.value
    })
  }
 
    handleDivClick(item: any): void {
      this.selectedItemId = this.selectedItemId === item.id ? null : item.id;
      this.showDetails = this.selectedItemId !== null;
    }
  
    itemChosen = false
    selectedChosenItem: any;
  
    onClick(item: any): void {
      this.itemChosen = true;
      this.selectedChosenItem = item;
    }
  
    goToUpload(): void {
      this.router.navigate(['upload-items'])
    }
  
    getName(): void {
      this.name = sessionStorage.getItem("full_name")
      this.admin = sessionStorage.getItem("admin")
    }

  }


