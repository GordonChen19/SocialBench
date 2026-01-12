from typing import List, Optional
from pydantic import BaseModel, Field
import extraction_chain.data_type as dt

class PerceptionLayer(BaseModel):
    """
    The Raw Signal Processing Layer.
    Captures WHAT is happening before determining WHY.
    """
    visual_cues: List[str] = Field(description="Specific visual cues (e.g., 'Brow furrowed implies concern', 'Clenched Fists implies anger', 'Smiling without eyes implies insincerity', 'Man walks Back and Forth in the meeting implies confidence').")
    audio_cues: List[str] = Field(description="Specific audio signals (e.g., 'Long Pauses implies hesitation', 'High Volume implies excitement', 'Trembling voice implies fear').")
    textual_cues: List[str] = Field(description="Specific textual signals (e.g., ''Thank you' implies politeness', ''You listen to me' implies autority'.")
    congruence_check: dt.CrossModalCongruence
    temporal_dynamics: dt.TemporalDynamics

class SocialNormativeContext(BaseModel):
    """
    Analyzes the rules, setting, and cultural framework.
    """
    permeability: dt.Permeability = Field(
        description="How strict is the filter for this interaction? Does it block outsiders from entering (Physical), and block private details from being shared (Informational)?"
    )
    topology: dt.Topology = Field(
        description="How are the agents grouped? Are they acting as a single unit (Unified), separate dyads, or fragmented atoms?"
    )
    size_category: dt.SizeCategory = Field(
        description="What is the magnitude of participants involved (e.g., a couple, a small team, or a mob)?"
    )
    focus_level: dt.FocusLevel = Field(
        description="Is the group's attention unified on a single subject/speaker, or is it fragmented?"
    )
    orientation: dt.Orientation = Field(
        description="Does the physical geometry of the agents face inward to encourage connection (Sociopetal) or outward to discourage it (Sociofugal)?"
    )
    norm_constraint: dt.NormConstraint = Field(
        description="How strict are the rules here? Is this a 'Tight' culture (one right way to act) or a 'Loose' culture (anything goes)?"
    )
    norm_enforcement_strength: dt.NormEnforcementStrength = Field(
        description="If a norm were violated, how immediate and severe would the social correction be?"
    )
    turn_taking_regime: dt.TurnTakingRegime = Field(
        description="How is the floor managed? Is speaking spontaneous, strictly ordered by authority, or chaotic?"
    )
    interaction_density: dt.InteractionDensity = Field(
        description="What is the pace of communication? Is it rapid-fire (Dense) or slow/sparse?"
    )
    participation_access: dt.ParticipationAccess = Field(
        description="Who has the right to speak? Is the floor open to anyone, or gated by specific roles/status?"
    )
    temporal_pressure: dt.TemporalPressure = Field(
        description="Is there urgency? Are the agents acting under the pressure of a deadline or immediate threat?"
    )
    stakes_level: dt.StakesLevel = Field(
        description="What is at risk? Are the consequences of failure trivial, material (money/safety), or symbolic (honor/reputation)?"
    )
    expected_valence: dt.ExpectedValence = Field(
        description="What emotional tone does this setting demand? Should agents be somber, neutral, or expressive?"
    )
    
    # Note: verdict is the answer to the sum of the questions above
    verdict: dt.NormVerdict = Field(
        description="Based on the answers above, did the agent's behavior adhere to the constraints or violate them?"
    )

class CommunicativeIntent(BaseModel):
    """
    Analyzes the purpose, strategy, and content of a specific action/utterance.
    """
    speech_act: dt.SpeechActType = Field(
        description="What is the mechanical function of this utterance? Is the speaker giving an order, stating a fact, making a promise, or expressing an emotion?"
    )

    politeness_strategy: dt.PolitenessStrategy = Field(
        description="How much 'social cushion' did the speaker wrap around the message? Did they attack the listener's face, protect it with politeness, or ignore it entirely?"
    )
    
    social_vector: dt.SocialVector = Field(
        description="What is the directional impact on the relationship? Is the speaker trying to pull the listener closer (Affiliative) or push them away/dominate them (Adversarial)?"
    )
    
    response_expectation: dt.ResponseExpectation = Field(
        description="Does this utterance create a social debt? Is the listener explicitly obligated to reply or act, or is the floor now closed?"
    )

    sincerity_mode: dt.SincerityMode = Field(
        description="Is the speaker being genuine, ironic, or deceptive in their intent?"
    )


    intent_category: dt.IntentCategory = Field(
        description="What is the high-level purpose of this communicative act?")
    
    intent_causal_reasoning: str = Field(
        description="Detailed explanation of why the Agent is pursuing this intent."
    )
    
    # rationale_description: str = Field(
    #     description="Detailed explanation. (e.g., 'Agent A used sarcasm to vent anger (Expressive) while maintaining the option to say 'I was just joking' if Agent B got aggressive (Deniability)')."
    # )

class RelationshipContext(BaseModel):
    """
    Analyzes the static bond between the agents *before* the current interaction starts.
    """

    relationship_type: dt.RelationshipCategory = Field(
        description="What is the official label for this relationship? (e.g., Is this a work meeting or a family dinner?)"
    )
    
    intimacy_level: dt.IntimacyLevel = Field(
        description="How thick is the psychological wall between them? Are they strangers or soulmates?"
    )
    
    power_dynamic: dt.PowerDynamic = Field(
        description="Who holds the structural authority? Is it a peer-to-peer exchange or a boss-employee dynamic?"
    )

    power_causality: Optional[dt.RelationshipCausality] = Field(
        None,
        description="Deep dive into the 'Why' of the power and trust dynamics."
    )
    
    trust_level: dt.TrustLevel = Field(
        description="What is the baseline level of safety? Do they expect the other person to help them or hurt them?"
    )

    relationship_valence : dt.RelationshipValence = Field(
        description="What is the general emotional tone of the relationship? Is it positive, negative, or neutral?"
    )   
    relationship_trajectory: dt.RelationshipTrajectory = Field(
        description="Is the relationship improving, deteriorating, or stable over time?"
    )
    relationship_change_trigger: Optional[str] = Field(
        None, 
        description="What specific event in this scene or in the past explain why the relationship is moving in such trajectory? (e.g., 'Agent A's confession shifted Trust from High to Broken')."
    )


class EmotionContext(BaseModel):
    """
    Analyzes the agent's internal state and external display.
    """

    felt_emotion: dt.EmotionCategory = Field(
        description="What the agent is genuinely feeling inside, regardless of what they show."
    )
    
    arousal_level: dt.ArousalLevel = Field(
        description="How intense is this feeling? (e.g., Is it 'Annoyance' or 'Rage'?)"
    )
    
    valence: dt.ValenceType = Field(
        description="Is this feeling pleasant or painful?"
    )

    displayed_emotion: dt.EmotionCategory = Field(
        description="What emotion is the agent showing to the world? (May differ from Felt Emotion)."
    )
    
    display_rule: dt.DisplayRule = Field(
        description="Is the agent faking, hiding, or exaggerating this emotion? (e.g., 'Smiling through the pain' = Masked)."
    )

    trigger_event: str = Field(
        description="What specific event, word, or thought caused this emotion and why did the trigger lead to this emotion? (e.g., 'Agent B's insult', 'The realization that the deadline passed')."
    )

class ComprehensionLayer(BaseModel):
    """
    Captures the Observable Status of the scene.
    """
    social_normative_context: SocialNormativeContext
    relationship_power_dynamics: RelationshipContext
    emotional_state: EmotionContext
    communicative_intent: CommunicativeIntent

class ResponseLayer(BaseModel):
    pass
