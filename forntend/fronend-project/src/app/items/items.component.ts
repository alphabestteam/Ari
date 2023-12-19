import { Component } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})

export class ItemsComponent {
  items: any[] = [];
  selectedItemId: any;
  showDetails: boolean = false;
  name: any

  constructor(private itemService: ItemService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.fetchItems();
    this.getName()
  }

  fetchItems(): void {
    this.itemService.getItems().subscribe(
      (data: any[]) => {
        this.items = data.map(item => ({ ...item, clicked: false }));

      },
      (error) => {
        console.error('Error fetching items:', error);
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
    // this.goToTaken()
  }

  goToUpload(): void {
    this.router.navigate(['upload-items'])
  }

  goToTaken(): void {
    this.router.navigate(['taken-items'])
  }

  getName() :void {
    this.name = sessionStorage.getItem("full_name")
  }
}
