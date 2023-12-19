import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TakenItemsComponent } from './taken-items.component';

describe('TakenItemsComponent', () => {
  let component: TakenItemsComponent;
  let fixture: ComponentFixture<TakenItemsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TakenItemsComponent]
    });
    fixture = TestBed.createComponent(TakenItemsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
