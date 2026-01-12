from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Perception Layer ---
class CongruenceStatus(str, Enum):
    CONGRUENT = "Congruent"
    INCONGRUENT = "Incongruent"

class CrossModalCongruence(BaseModel):
    status: CongruenceStatus = Field(description="Overall alignment of the three modalities.")
    explanation: str = Field(description="Rationale for the congruence assessment.")

class TemporalDynamics(BaseModel):
    visual_change: str = Field(description="How visual cues evolve over time (e.g., 'Smile slowly turns into a frown', 'Mouth begins to tremble').")
    audio_change: str = Field(description="How audio cues evolve over time (e.g., 'Rising Pitch', 'Volume increases', 'stuttering').")
    textual_change: str = Field(description="How textual cues evolve over time (e.g., )")

# --- Social Context ---

class Permeability(str, Enum):
    CLOSED_PRIVATE = "Closed (Private)"
    OPEN_PUBLIC = "Open (Public)"

class Topology(str, Enum):

    ATOMIZED = "Atomized (Independent agents, parallel activity, no links)"
    DYADIC = "Dyadic (Exclusive 1-on-1 interaction)"
    CENTRALIZED = "Centralized (Hub-and-Spoke, focus on single leader/object)"
    DISTRIBUTED = "Distributed (Mesh network, free-flowing many-to-many)"
    CLUSTERED = "Clustered (Distinct subgroups/cliques interacting internally)"
    SEQUENTIAL = "Sequential (Round-robin, turn-taking passed in a loop)"
    POLARIZED = "Polarized (Group explicitly united *against* or *ignoring* an outsider)"

class SizeCategory(str, Enum):
    SOLO = "Solo (1)"
    DYADIC = "Dyadic (2)"
    TRIADIC = "Triadic (3)"
    SMALL_GROUP = "Small Group (4-10)"
    LARGE_GROUP = "Large Group (11+)"

class FocusLevel(str, Enum):
    HIGH_FOCUS = "High Focus (All Eyes on Subject)"
    MODERATE_FOCUS = "Moderate Focus (Some Attention on Subject)"
    LOW_FOCUS = "Low Focus (Attention is Dispersed)"

class Orientation(str, Enum):
    SOCIOPETAL = "Sociopetal (Encourages Interaction)"
    SOCIOFUGAL = "Sociofugal (Discourages Interaction)"
    NEUTRAL = "Neutral (Neither Encourages nor Discourages Interactions)"

class NormConstraint(str, Enum):
    TIGHT = "Tight (Strict Adherence)"
    LOOSE = "Loose (Permissive)"
    AMBIGUOUS = "Ambiguous (Unclear Expectations)"

class NormEnforcementStrength(str, Enum):
    WEAK = "Weak (Rarely Enforced)"
    IMPLICIT = "Implicit (Socially Enforced)"
    STRONG = "Strong (Formally Enforced via Rules, Authority, Punishment)"

# class Temporality(str, Enum):
#     TRANSIENT = "Transient (Short Duration Interaction)"
#     EXTENDED = "Extended (Long Duration Interaction)"

class TurnTakingRegime(str, Enum):
    REGULATED = "Regulated (Formal turns, moderator-controlled)"
    SEMI_REGULATED = "Semi-Regulated (Implicit politeness norms)"
    UNREGULATED = "Unregulated (Free overlap, interruptions allowed)"

class InteractionDensity(str, Enum):
    SPARSE = "Sparse (Long pauses, infrequent turns, Single person speaking)"
    MODERATE = "Moderate (Balanced exchange)"
    DENSE = "Dense (Rapid turns, high verbal activity)"

class ParticipationAccess(str, Enum):
    OPEN = "Open (Anyone may speak)"
    ROLE_GATED = "Role-Gated (Only specific roles may speak)"
    CONDITIONAL = "Conditional (Only when prompted or sanctioned)"

class TemporalPressure(str, Enum):
    LOW = "Low (No urgency)"
    MEDIUM = "Medium (Time-aware but flexible)"
    HIGH = "High (Urgent, compressed interaction)"

class StakesLevel(str, Enum):
    LOW = "Low Stakes (Social / Recreational)"
    MEDIUM = "Medium Stakes (Reputation / Mild Conflict)"
    HIGH = "High Stakes (Career / Safety / Legal / Life)"

class ExpectedValence(str, Enum):
    POSITIVE = "Positive (Supportive, Affirming)"
    NEUTRAL = "Neutral (Objective, Unbiased)"
    NEGATIVE = "Negative (Critical, Confrontational)"

class VERDICT (str, Enum):
    ADHERENCE = "Adherence"
    VIOLATION = "Violation"
    AMBIGUOUS = "Ambiguous"

class CategoryViolation(str, Enum):
    PERMEABILITY = "permeability"
    TOPOLOGY = "topology"
    SIZE_CATEGORY = "size_category"
    FOCUS_LEVEL = "focus_level"
    ORIENTATION = "orientation"
    NORM_CONSTRAINT = "norm_constraint"
    NORM_ENFORCEMENT_STRENGTH = "norm_enforcement_strength"
    TURN_TAKING_REGIME = "turn_taking_regime"
    INTERACTION_DENSITY = "interaction_density"
    PARTICIPATION_ACCESS = "participation_access"
    TEMPORAL_PRESSURE = "temporal_pressure"
    STAKES_LEVEL = "stakes_level"
    ROLE_STABILITY = "role_stability"
    EXPECTED_VALENCE = "expected_valence"

class ViolationCause(str, Enum):
    IGNORANCE = "Ignorance (Agent did not know the rule - e.g., Tourist/Child)"
    INCAPACITY = "Incapacity (Agent physically/mentally could not follow rule - e.g., Sneeze, Panic)"
    PRIORITIZATION = "Prioritization (Agent deliberately chose a higher goal - e.g., Emergency, Profit)"
    DEFIANCE = "Defiance (Agent broke rule specifically to send a message - e.g., Protest, Insult)"
    ACCIDENTAL = "Accidental (Unintended slip - e.g., Dropping a glass)"

class SpecificViolation(BaseModel):
    """
    Detailed breakdown of a specific rule breach.
    """
    # This links the crime back to the specific 'active_constraint'
    target_category: str = Field(..., description="Must match the 'target_category' of the constraint that was broken.")
    
    cause_category: ViolationCause = Field(
        description="The fundamental reason for the breach."
    )

    competing_force: str = Field(
        description="What specific drive overpowered the social norm? (e.g., 'Extreme Pain', 'Urgent Deadline', 'Desire to humiliate Agent B')."
    )
    # The Evidence
    expected_behavior: str = Field(..., description="What the constraint required (e.g., 'Silence').")
    observed_behavior: str = Field(..., description="What the agent actually did (e.g., 'Yelled').")
    
    is_excusable: bool = Field(
        description="Given the cause, would a reasonable observer forgive this violation? (e.g., True for 'Heart Attack', False for 'Drunk')."
    )

class NormVerdict(BaseModel):
    judgment: VERDICT = Field(..., description="Adherence, Violation, or Ambiguous")
    
    # If Judgment == Violation, this list populates.
    violations: Optional[SpecificViolation] = Field(
        default=[], 
        description="A list of specific constraints that were broken."
    )
    
# class RoleStability(str, Enum):
#     FIXED = "Fixed (Stable, uncontested roles)"
#     FLUID = "Fluid (Roles shift naturally)"
#     CONTESTED = "Contested (Actors compete for authority/floor)"

# --- Communicative Intent ---

class SpeechActType(str, Enum):
    DIRECTIVE = "Directive (Orders, Requests, Advice, Warnings)" 
    ASSERTIVE = "Assertive (Statements, Claims, Predictions, Dissent)"
    COMMISSIVE = "Commissive (Promises, Threats, Offers, Vows)"
    EXPRESSIVE = "Expressive (Apologies, Thanks, Congratulations, Venting)"
    DECLARATIVE = "Declarative (Rituals: 'You're fired', 'I quit')"
    PHATIC = "Phatic (Channel checks: 'Hello', 'Can you hear me?')"
    WITHHOLDING = "Withholding (Intentional silence / non-response)"

class SocialVector(str, Enum):
    AFFILIATIVE = "Affiliative (Bonding, Repairing, Supporting)"
    ADVERSARIAL = "Adversarial (Attacking, Dominating, Criticizing)"
    NEUTRAL = "Neutral (Transactional, Objective)"
    AMBIGUOUS = "Ambiguous (Unclear or Mixed)"

class ResponseExpectation(str, Enum):
    REQUIRED = "Required (Answer/action expected)"
    OPTIONAL = "Optional (Response welcome but not required)"
    NONE = "None (No response expected)"

class SincerityMode(str, Enum):
    SINCERE = "Sincere (Aligned with internal state)"
    STRATEGIC = "Strategic (Instrumental, face-managed)"
    DECEPTIVE = "Deceptive (Intentionally misleading)"
    PERFORMATIVE = "Performative (Ritual / audience-facing)"

#How much face-risk the speaker is willing to tolerate to achieve their communicative goal (Brown & Levinson)
class PolitenessStrategy(str, Enum):
    """How the speaker manages the listener's 'Face'."""
    BALD_ON_RECORD = "Bald on Record (Direct, no softening: 'Give me that.')"
    POSITIVE_POLITENESS = "Positive Politeness (Boosting the listener: 'Hey buddy, can you help?')"
    NEGATIVE_POLITENESS = "Negative Politeness (Minimizing imposition: 'Sorry to bother you, but...')"
    OFF_RECORD = "Off Record (Vague/Indirect hint: 'It's cold in here' -> 'Close the window')"
    HOSTILE = "Hostile (Active attack on face: Insults, Snapping)"

class IntentCategory(str, Enum):
    # --- INTERNAL DRIVERS ---
    INTERNALIZED_VALUE = "Internalized Value (Agent acts out of personal honor/morality)"
    ALTRUISM = "Altruism (Agent acts to help the other, regardless of reward)"
    HABITUAL = "Habitual (Agent acts on autopilot/script without thinking)"
    
    # --- EXTERNAL/RELATIONAL DRIVERS ---
    RECIPROCITY = "Reciprocity (Agent acts to balance the Social Ledger / Repay debt)"
    COMPLIANCE = "Compliance (Agent acts to avoid punishment/judgment)"
    RELATIONAL_MAINTENANCE = "Relational Maintenance (Agent acts to preserve the bond)"
    
    # --- STRATEGIC DRIVERS ---
    INSTRUMENTAL_GAIN = "Instrumental Gain (Agent acts to get a future reward)"
    SIGNALING = "Signaling (Agent acts to prove status/virtue to an audience)"

# --- Relationships ---
class RelationshipCategory(str, Enum):
    """The broad label for the tie."""
    PROFESSIONAL = "Professional (Colleagues, Boss-Employee, Team)"
    TRANSACTIONAL = "Transactional (Service Providers, Clerks, Functional Exchange)"
    SOCIAL = "Social (Friends, Neighbors, Civil Peers, Leisure Contexts)"
    FAMILIAL = "Familial (Blood relatives, In-laws)"
    ROMANTIC = "Romantic (Partners, Dates, Exes)"
    ANTAGONISTIC = "Antagonistic (Rivals, Enemies, Opponents)"

class IntimacyLevel(str, Enum):
    """The depth of psychological closeness (Self-Disclosure)."""
    STRANGER = "Stranger (No history, no disclosure)"
    ACQUAINTANCE = "Acquaintance (Surface info, 'Weak Tie')"
    FRIEND = "Friend (Moderate disclosure, emotional support)"
    CLOSE_INTIMATE = "Close/Intimate (Deep vulnerability, 'Thick Tie')"

class PowerDynamic(str, Enum):
    """The static balance of power between agents."""
    SYMMETRICAL = "Symmetrical (Peers, Equals)"
    HIERARCHICAL = "Hierarchical (Clear Superior/Subordinate definition)"
    COMPETITIVE = "Competitive (Unstable or challenged hierarchy)"

class TrustLevel(str, Enum):
    """The baseline expectation of safety."""
    HIGH = "High (Psychological safety, benefit of the doubt)"
    NEUTRAL = "Neutral (Guarded, 'Trust but Verify')"
    LOW = "Low (Suspicion, hesitation)"
    BROKEN = "Broken (Active betrayal, hostile expectations)"

class RelationshipValence(str, Enum):
    POSITIVE = "Positive (Warm, cooperative)"
    NEUTRAL = "Neutral (Functional, detached)"
    NEGATIVE = "Negative (Tense, resentful)"
    AMBIVALENT = "Ambivalent (Mixed signals)"

class RelationshipTrajectory(str, Enum):
    STABLE = "Stable (No meaningful change)"
    IMPROVING = "Improving (Repair, bonding, trust gain)"
    DETERIORATING = "Deteriorating (Erosion, conflict)"
    FRACTURING = "Fracturing (Breakdown imminent)"
    REPAIRING = "Repairing (Post-conflict recovery)"

class PowerSource(str, Enum):
    LEGITIMATE = "Legitimate (Official rank/authority)"
    COERCIVE = "Coercive (Fear of punishment/force)"
    REWARD = "Reward (Control over resources/money)"
    EXPERT = "Expert (Superior knowledge/skill)"
    REFERENT = "Referent (Admiration/Loyalty/Charisma)"
    INFORMATIONAL = "Informational (Blackmail/leverage via asymmetry)"

class RelationshipCausality(BaseModel):
    """
    Explains the mechanics of the relationship. 
    Why is the power dynamic this way? What sustains the bond?
    """

    # --- 1. POWER DIAGNOSTICS (The Source) ---
    primary_power_source: Optional[PowerSource] = Field(
        None,
        description="If the dynamic is Hierarchical, what gives the Superior their power? (e.g., Is it 'Expert' because they know the code, or 'Legitimate' because they are the Manager?)"
    )
    
    power_stability_analysis: str = Field(
        description="Causal logic: Is the power dynamic stable? (e.g., 'Unstable because it relies on Coercion, which breeds resentment' vs 'Stable because it relies on Referent trust')."
    )
    
    relationship_change_trigger: Optional[str] = Field(
        None, 
        description="What specific event in this scene or in the past explain why the relationship is moving in such trajectory? (e.g., 'Agent A's confession shifted Trust from High to Broken')."
    )



# --- Emotions ---

class EmotionCategory(str, Enum):
    """
    The dominant emotional state.
    Includes Ekman's Basic 6 + Complex Social Emotions essential for conflict/bonding.
    """
    # --- Basic (Ekman) ---
    JOY = "Joy (Happiness, Amusement, Relief)"
    SADNESS = "Sadness (Grief, Disappointment, Despair)"
    ANGER = "Anger (Frustration, Rage, Irritation)"
    FEAR = "Fear (Anxiety, Terror, Apprehension)"
    DISGUST = "Disgust (Revulsion, Contempt, Loathing)"
    SURPRISE = "Surprise (Shock, Astonishment)"
    
    # --- Social / Self-Conscious (The "Driver" Emotions) ---
    SHAME = "Shame (Feeling exposed/worthless - 'I am bad')"
    GUILT = "Guilt (Feeling remorse for action - 'I did something bad')"
    PRIDE = "Pride (Feeling superior/accomplished)"
    ENVY = "Envy (Wanting what another has)"
    JEALOUSY = "Jealousy (Fear of losing something to another)"
    EMBARRASSMENT = "Embarrassment (Social awkwardness/accident)"
    
    # --- Cognitive States ---
    CONFUSION = "Confusion (Uncertainty, Disorientation)"
    INTEREST = "Interest (Curiosity, Engagement)"
    BOREDOM = "Boredom (Disengagement, Apathy)"
    NEUTRAL = "Neutral (Baseline, Calm)"

class ArousalLevel(str, Enum):
    """The intensity or energy level of the emotion."""
    LOW = "Low (Subdued, Calm, Depressed)"
    MODERATE = "Moderate (Active, Noticeable)"
    HIGH = "High (Intense, Overwhelming, Visceral)"
    EXTREME = "Extreme (Out of control, Hysterical, Blind Rage)"

class ValenceType(str, Enum):
    """The intrinsic 'goodness' or 'badness' of the feeling."""
    POSITIVE = "Positive (Pleasant)"
    NEGATIVE = "Negative (Unpleasant)"
    NEUTRAL = "Neutral"

class DisplayRule(str, Enum):
    """
    How the agent is managing the expression of this emotion (Ekman & Friesen).
    Crucial for detecting Deception/Politeness.
    """
    AMPLIFIED = "Amplified (Exaggerating the feeling - e.g., Faking excitement)"
    DEAMPLIFIED = "Deamplified (Downplaying the feeling - e.g., 'I'm fine')"
    NEUTRALIZED = "Neutralized (Poker face - Hiding all emotion)"
    MASKED = "Masked (Replacing true emotion with a fake one - e.g., Smiling while angry)"
    GENUINE = "Genuine (Expression matches internal state)"