import { Component } from '@angular/core';
import { ItemService } from '../item.service'
import { Router } from '@angular/router';
@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})

export class ItemsComponent {
  items: any[] = [];
  takenItems: any[] = [];

  name: any
  admin : any

  selectedItemId: any;
  showDetails: boolean = false;
  
  constructor(private itemService: ItemService, private router: Router,) { } 

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

  handleDivClick(item: any): void {
    this.selectedItemId = item.id;
    this.showDetails = !this.showDetails;
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

  getName() :void {
    this.name = sessionStorage.getItem("full_name")
    this.admin = sessionStorage.getItem("admin")
  }
}
