from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    Text
)

from sqlalchemy.orm import declarative_base

from datetime import datetime


# ==========================================
# DATABASE BASE
# ==========================================

Base = declarative_base()


# ==========================================
# PATIENT DATABASE MODEL
# ==========================================

class PatientDB(Base):

    __tablename__ = "patients"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    age = Column(
        Integer,
        nullable=True
    )

    gender = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    address = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# GAME SCORE DATABASE MODEL
# ==========================================

class GameScoreDB(Base):

    __tablename__ = "game_scores"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    game_name = Column(
        String,
        nullable=False
    )

    score = Column(
        Integer,
        nullable=False
    )

    accuracy = Column(
        Float,
        nullable=True
    )

    time_taken = Column(
        Float,
        nullable=True
    )

    difficulty = Column(
        String,
        nullable=True
    )

    played_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# GAME PROGRESS DATABASE MODEL
# ==========================================

class GameProgressDB(Base):

    __tablename__ = "game_progress"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    game_name = Column(
        String,
        nullable=False
    )

    level = Column(
        Integer,
        default=1
    )

    highest_score = Column(
        Integer,
        default=0
    )

    total_games = Column(
        Integer,
        default=0
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


# ==========================================
# REMINDER DATABASE MODEL
# ==========================================

class ReminderDB(Base):

    __tablename__ = "reminders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    reminder_time = Column(
        DateTime,
        nullable=False
    )

    completed = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# MEMORY DATABASE MODEL
# ==========================================

class MemoryDB(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    memory_date = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# ALERT DATABASE MODEL
# ==========================================

class AlertDB(Base):

    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    message = Column(
        Text,
        nullable=False
    )

    alert_type = Column(
        String,
        default="general"
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# CAREGIVER DATABASE MODEL
# ==========================================

class CaregiverDB(Base):

    __tablename__ = "caregivers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    relationship = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    email = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# FAMILY MEMBER DATABASE MODEL
# ==========================================

class FamilyMemberDB(Base):

    __tablename__ = "family_members"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    relationship = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )