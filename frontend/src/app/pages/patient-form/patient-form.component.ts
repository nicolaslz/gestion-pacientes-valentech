import { Component } from '@angular/core';
import { Patient } from '../../models/patient.model';
import { PatientService } from '../../services/patient.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-patient-form',
  templateUrl: './patient-form.component.html',
  styleUrls: ['./patient-form.component.scss']
})
export class PatientFormComponent {
  patient: Patient = {
    name: '',
    document: '',
    email: '',
    phone: '',
    disease: ''
  };
  toastMessage: string = '';
  toastType: 'success' | 'error' = 'success';
  showToast: boolean = false;
  loading: boolean = false;
  submitted: boolean = false;
  constructor(private patientService: PatientService, private router: Router) {}

  submit(form: any) {
    this.submitted = true;

    if (form.invalid) {
      this.toastType = 'error';
      this.toastMessage = 'Por favor completa todos los campos correctamente antes de continuar.';
      this.showToast = true;
      setTimeout(() => this.showToast = false, 5000);
      return;
    }

    this.loading = true;

    this.patientService.createPatient(this.patient).subscribe({
      next: (response) => {
        this.toastMessage = 'Paciente registrado exitosamente';
        this.toastType = 'success';
        this.showToast = true;
        this.patient = { name: '', document: '', email: '', phone: '', disease: '' };

        setTimeout(() => {
          this.showToast = false;
          this.loading = false;
          this.router.navigate(['/list']);
        }, 1000);
      },
      error: (err) => {
        this.toastMessage = err?.error?.error || 'Ocurrió un error al registrar el paciente';
        this.toastType = 'error';
        this.showToast = true;

        setTimeout(() => {
          this.showToast = false;
          this.loading = false;
        }, 5000);
      }
    });
  }


}
