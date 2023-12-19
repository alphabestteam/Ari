import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { HomeComponent } from './home/home.component';
import { UploadItemsComponent } from './upload-items/upload-items.component';
import { TakenItemsComponent } from './taken-items/taken-items.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component'

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignUpComponent },
  { path: 'home', component: HomeComponent },
  { path: 'upload-items', component: UploadItemsComponent },
  { path: 'taken-items', component: TakenItemsComponent },
  { path: 'personal-area', component: PersonalAreaComponent },
  { path: '**', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
