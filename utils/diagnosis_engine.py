"""
Diagnosis Engine Module
========================

Core logic for symptom analysis and disease probability calculation.
"""

from typing import Dict, List, Tuple, Any
import logging

logger = logging.getLogger(__name__)

class DiagnosisEngine:
    """Handles disease probability calculations and diagnosis"""

    def __init__(self, disease_database: Dict[str, Any]):
        self.disease_database = disease_database

    def calculate_disease_probability(
        self,
        symptoms_data: Dict[str, int],
        disease_info: Dict[str, Any]
    ) -> Tuple[float, List[str]]:
        """
        Calculate probability of disease based on symptom matching

        Args:
            symptoms_data: Dictionary of symptom names to severity (0-10)
            disease_info: Disease configuration from database

        Returns:
            Tuple of (probability, list of matched symptoms)
        """
        matched_score = 0
        total_possible = 0
        matched_symptoms = []

        disease_symptoms = disease_info.get('symptoms', {})

        for symptom, weight in disease_symptoms.items():
            total_possible += weight * 10
            if symptom in symptoms_data and symptoms_data[symptom] > 0:
                symptom_value = symptoms_data[symptom]
                matched_score += (symptom_value * weight)
                if symptom_value >= 5:
                    matched_symptoms.append(symptom.replace('_', ' ').title())

        probability = (matched_score / total_possible) * 100 if total_possible > 0 else 0
        return probability, matched_symptoms

    def adjust_probability_by_temperature(
        self,
        probability: float,
        temperature: float,
        disease_info: Dict[str, Any]
    ) -> float:
        """
        Adjust disease probability based on temperature range match

        Args:
            probability: Current probability score
            temperature: Patient's temperature
            disease_info: Disease configuration

        Returns:
            Adjusted probability
        """
        temp_range = disease_info.get('temp_range', [0, 100])

        # Check if temperature is within disease range
        if temp_range[0] <= temperature <= temp_range[1]:
            probability *= 1.2
        elif abs(temperature - temp_range[1]) <= 1.0:
            probability *= 1.1

        return min(probability, 100)

    def analyze_symptoms(
        self,
        symptoms_data: Dict[str, int],
        temperature: float,
        min_confidence: float = 20
    ) -> List[Dict[str, Any]]:
        """
        Analyze symptoms and return potential diagnoses

        Args:
            symptoms_data: Dictionary of symptom severities
            temperature: Patient's temperature
            min_confidence: Minimum confidence threshold

        Returns:
            List of potential diagnoses sorted by confidence
        """
        disease_matches = []

        for disease_name, disease_info in self.disease_database.items():
            # Calculate base probability
            probability, matched_symptoms = self.calculate_disease_probability(
                symptoms_data, disease_info
            )

            # Adjust for temperature
            probability = self.adjust_probability_by_temperature(
                probability, temperature, disease_info
            )

            # Only include if above threshold
            if probability >= min_confidence:
                disease_matches.append({
                    'disease': disease_name,
                    'description': disease_info.get('description', disease_name),
                    'confidence': round(probability, 1),
                    'urgency': disease_info.get('urgency', 'normal'),
                    'severity': disease_info.get('severity', 'medium'),
                    'matched_symptoms': matched_symptoms,
                    'incubation': disease_info.get('incubation', 'unknown')
                })

        # Sort by confidence (highest first)
        disease_matches.sort(key=lambda x: x['confidence'], reverse=True)

        logger.info(f"Found {len(disease_matches)} potential diagnoses")
        return disease_matches

    def assess_overall_severity(
        self,
        diagnoses: List[Dict[str, Any]],
        symptoms_data: Dict[str, int],
        temperature: float
    ) -> int:
        """
        Assess overall patient condition severity (0-10 scale)

        Args:
            diagnoses: List of potential diagnoses
            symptoms_data: Symptom severity data
            temperature: Patient's temperature

        Returns:
            Severity score (0-10)
        """
        severity_score = 0

        # Temperature contribution
        if temperature >= 40.0:
            severity_score += 4
        elif temperature >= 39.0:
            severity_score += 3
        elif temperature >= 38.0:
            severity_score += 2
        elif temperature >= 37.5:
            severity_score += 1

        # Critical symptoms
        high_severity_symptoms = ['difficulty_breathing', 'chest_pain', 'confusion']
        for symptom in high_severity_symptoms:
            symptom_value = symptoms_data.get(symptom, 0)
            if symptom_value >= 7:
                severity_score += 3
            elif symptom_value >= 5:
                severity_score += 2

        # Average symptom severity
        if symptoms_data:
            symptom_avg = sum(symptoms_data.values()) / len(symptoms_data)
            if symptom_avg >= 7:
                severity_score += 3
            elif symptom_avg >= 5:
                severity_score += 2
            elif symptom_avg >= 3:
                severity_score += 1

        # Disease confidence and urgency
        if diagnoses and diagnoses[0]['confidence'] >= 80:
            if diagnoses[0]['urgency'] == 'urgent':
                severity_score += 2
            elif diagnoses[0]['urgency'] == 'warning':
                severity_score += 1

        return min(severity_score, 10)

