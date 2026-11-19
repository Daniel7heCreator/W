DATABASE_URL = "postgresql+psycopg2://postgres:nicedogboy228@localhost:5432/test"
import datetime

from sqlalchemy import create_engine, text, select
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine(DATABASE_URL,echo=True)

class Base(DeclarativeBase):
    pass

class Recording(Base):
    __tablename__ = "recordings"
    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    appointment_time: Mapped[datetime.datetime] = mapped_column()
    status: Mapped[str] = mapped_column(String(20))

class Doctor(Base):
    __tablename__ = "doctors"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150))
    cabinet_number: Mapped[str] = mapped_column(String(10))

class Patient(Base):
    full_name: Mapped[str] = mapped_column(String(150))
    birth_date: Mapped[datetime.date] = mapped_column()
    phone_number: Mapped[str] = mapped_column(String(20))
    policy_number: Mapped[str] = mapped_column(String(30))

class RecordingDiagnosis(Base):
    __tablename__ = "recording_diagnoses"
    recording_id: Mapped[int] = mapped_column(ForeignKey("recordings.id"))
    icd_code_id: Mapped[int] = mapped_column(ForeignKey("ice_codes.id"))
    type: Mapped[str] = mapped_column(String(50))

class Icd_code(Base):
    __tablename__ = "ice_codes"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(10))
    title: Mapped[str] = mapped_column(String(None))

class Service(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    price: Mapped[int] = mapped_column()

class Speciality(Base):
    __tablename__ = "specialties"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class DoctorSpeciality(Base):
    __tablename__ = "doctor_specialties"
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    speciality_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"))