import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { HomeComponent } from './home/home.component';
import { UploadItemsComponent } from './upload-items/upload-items.component';
import { TakenItemsComponent } from './taken-items/taken-items.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component'
import { EditItemsComponent } from './edit-items/edit-items.component'
import { WelcomeComponent } from './welcome/welcome.component'
import { authGuard } from './auth.guard';


const routes: Routes = [
  { path: 'login', component: LoginComponent},
  { path: 'signup', component: SignUpComponent },
  { path: 'home', component: HomeComponent, canActivate: [authGuard]},
  { path: 'upload-items', component: UploadItemsComponent, canActivate: [authGuard]},
  { path: 'taken-items', component: TakenItemsComponent, canActivate: [authGuard]},
  { path: 'personal-area', component: PersonalAreaComponent, canActivate: [authGuard]},
  { path: 'editItems/:id/:item_name/:city', component: EditItemsComponent, canActivate: [authGuard]},
  { path: 'welcome', component: WelcomeComponent, canActivate: [authGuard]},
  { path: '**', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
