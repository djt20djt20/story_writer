general_chat_response={
        "type": "json_schema",
        "json_schema": {
            "name": "user_profile",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "concept": {"type": "string"},
                    "main_quest": {"type": "array", "items": {"type": "string"}},
                    "stakes": {"type": "array", "items": {"type": "string"}},
                    "characters": {"type": "array", "items": {"type": "string"}},
                    "settings": {"type": "array", "items": {"type": "string"}},
                    "events": {"type": "array", "items": {"type": "string"}},
                    "main_plotlines": {"type": "array", "items": {"type": "string"}},
                    "subplots": {"type": "array", "items": {"type": "string"}},
                    "social_forces": {"type": "array", "items": {"type": "string"}},
                    "themes": {"type": "array", "items": {"type": "string"}},
                    "motifs": {"type": "array", "items": {"type": "string"}},
                    "villains": {"type": "array", "items": {"type": "string"}},
                    "mood": {"type": "array", "items": {"type": "string"}},
                    "conflicts": {"type": "array", "items": {"type": "string"}},
                    "target_audience": { "type": "string" },
                    "scenes": { "type": "array", "items": { "type": "string" }},
                    "symbolism": { "type": "array", "items": { "type": "string" }},
                    "climax": { "type": "string" },
                    "resolution": { "type": "string" },
                    "summary_long": { "type": "string" },
                    "summary_short": { "type": "string"}
                },
                "required": ["concept", "main_quest", "characters", "settings", "events","subplots", "main_plotlines", "social_forces", "themes", "motifs", "villains", "mood", "conflicts", "target_audience", "scenes", "symbolism", "climax", "resolution", "summary_long","summary_short"],
                "additionalProperties": False
            }
        }
}


settings_format={
        "type": "json_schema",
        "json_schema": {
            "name": "user_profile",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "description": {"type": "array", "items": {"type": "string"}},
                    "physical_features": {"type": "array", "items": {"type": "string"}},
                    "atmosphere": {"type": "array", "items": {"type": "string"}},
                    "weather": {"type": "array", "items": {"type": "string"}},
                    "sounds": {"type": "array", "items": {"type": "string"}},
                    "smells": {"type": "array", "items": {"type": "string"}},
                    "colors_and_visuals": {"type": "array", "items": {"type": "string"}},
                    "inhabitants": {"type": "array", "items": {"type": "string"}},
                    "cultural_or_historical_context": {"type": "array", "items": {"type": "string"}},
                    "objects_or_landmarks": {"type": "array", "items": {"type": "string"}},
                    "activities": {"type": "array", "items": {"type": "string"}},
                    "hazards_or_challenges": {"type": "array", "items": {"type": "string"}},
                    "feelings_or_reactions": { "type": "array", "items": { "type": "string" }},
                    "symbolic_importance": { "type": "array", "items": { "type": "string" }},
                    "short_summary": {"type": "string"},
                    "long_summary": {"type": "string"},
                },
                "required": ["description", "physical_features", "atmosphere", "weather","sounds", "smells", "colors_and_visuals", "inhabitants", "cultural_or_historical_context", "objects_or_landmarks", "activities", "hazards_or_challenges", "feelings_or_reactions", "symbolic_importance", "short_summary", "long_summary"],
                "additionalProperties": False
            }
        }
}

theme = {
    "type": "json_schema",
    "json_schema": {
        "name": "theme_profile",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "core_message": {"type": "string"},  # Main idea or takeaway
                "sub_themes": {"type": "array", "items": {"type": "string"}},  # Supporting ideas
                "moral_or_philosophical_questions": {"type": "array", "items": {"type": "string"}},  # Deeper questions raised
                "emotional_journey": {"type": "array", "items": {"type": "string"}},  # Feelings evoked in readers
                "motifs_and_symbols": {"type": "array", "items": {"type": "string"}},  # Recurring elements reinforcing the theme
                "connection_to_characters": {"type": "array", "items": {"type": "string"}},  # How the theme manifests in the characters' arcs
                "connection_to_plot": {"type": "array", "items": {"type": "string"}},  # How the theme is integrated into events or conflicts
                "target_audience_impact": {"type": "array", "items": {"type": "string"}},  # Desired effect on the audience
                "short_summary": {"type": "string"},
                "long_summary": {"type": "string"},
            },
            "required": [
                "core_message", 
                "sub_themes", 
                "moral_or_philosophical_questions", 
                "emotional_journey", 
                "motifs_and_symbols", 
                "connection_to_characters", 
                "connection_to_plot", 
                "target_audience_impact",
                "short_summary",
                'long_summary'
            ],
            "additionalProperties": False
        }
    }
}

concept = {
    "type": "json_schema",
    "json_schema": {
        "name": "concept_profile",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "core_concept": {"type": "string"},  # The central idea of the story
                "genre": {"type": "array", "items": {"type": "string"}},  # Genres that define the story
                "unique_angle": {"type": "string"},  # What makes the concept fresh or different
                "high_concept_pitch": {"type": "string"},  # A concise, one-sentence summary of the story
                "target_audience": {"type": "string"},  # Who the story is for
                "inspiration_or_origin": {"type": "string"},  # Where the idea came from
                "key_questions": {"type": "array", "items": {"type": "string"}},  # Questions the story aims to explore
                "potential_endings": {"type": "array", "items": {"type": "string"}},  # Possible resolutions for the story
                "thematic_resonance": {"type": "string"},  # How the concept ties into broader themes or messages
                "comp_titles_or_stories": {"type": "array", "items": {"type": "string"}},  # Comparable titles or inspirations
                "short_summary": {"type": "string"},
                "long_summary": {"type": "string"},
            },
            "required": [
                "core_concept", 
                "genre", 
                "unique_angle", 
                "high_concept_pitch", 
                "target_audience", 
                "key_questions", 
                "thematic_resonance",
                "comp_titles_or_stories",
                'short_summary',
                'long_summary'

            ],
            "additionalProperties": False
        }
    }
}

main_quest = {
    "type": "json_schema",
    "json_schema": {
        "name": "main_quest",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "protagonist_goal": {"type": "string"},  # The primary objective the protagonist is pursuing
                "stakes": {"type": "array", "items": {"type": "string"}},  # What is at risk if the protagonist fails
                "obstacles_and_challenges": {"type": "array", "items": {"type": "string"}},  # Major difficulties faced
                "allies_and_support": {"type": "array", "items": {"type": "string"}},  # Key allies or resources
                "antagonist_role": {"type": "string"},  # Role of the antagonist in the quest
                "resolution_and_reward": {"type": "string"},  # How the quest might be resolved and the outcome
                'short_summary': {"type": "string"},
                'long_summary': {"type": "string"}
            },
            "required": [
                "protagonist_goal", 
                "stakes", 
                "obstacles_and_challenges", 
                "antagonist_role", 
                "resolution_and_reward",
                'short_summary',
                'long_summary'
            ],
            "additionalProperties": False
        }
    }
}

stakes = {
    "type": "json_schema",
    "json_schema": {
        "name": "stakes",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "personal_stakes": {"type": "array", "items": {"type": "string"}},  # What the protagonist personally stands to lose or gain
                "global_stakes": {"type": "array", "items": {"type": "string"}},  # Broader consequences for the world or others
                "emotional_stakes": {"type": "array", "items": {"type": "string"}},  # Emotional impact or internal conflict
                "time_pressure": {"type": "array", "items": {"type": "string"}},  # Any time-sensitive elements that heighten urgency
                "moral_or_philosophical_stakes": {"type": "array", "items": {"type": "string"}},  # Ethical dilemmas or questions raised
                "symbolic_stakes": {"type": "array", "items": {"type": "string"}}, # What the stakes represent thematically or symbolically
                'short_summary': {"type": "string"},
                'long_summary': {"type": "string"}
            },
            "required": [
                "personal_stakes",
                "global_stakes",
                "emotional_stakes",
                "time_pressure",
                'time_pressure',
                'moral_or_philosophical_stakes',
                'symbolic_stakes',
                'short_summary',
                'long_summary'
            ],
            "additionalProperties": False
        }
    }
}

character = {
    "type": "json_schema",
    "json_schema": {
        "name": "character",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "role": {"type": "string"},  # Their role in the story (e.g., protagonist, mentor)
                "personality_traits": {"type": "array", "items": {"type": "string"}},  # Key traits defining their behavior
                "motivations": {"type": "array", "items": {"type": "string"}},  # What drives them
                "conflicts": {"type": "array", "items": {"type": "string"}},  # Their internal or external struggles
                "arc": {"type": "array", "items": {"type": "string"}},  # How they change or grow over the story
                "relationships": {"type": "array", "items": {"type": "string"}},  # Key relationships with other characters
                "strengths": {"type": "array", "items": {"type": "string"}},  # Skills or positive qualities
                "flaws": {"type": "array", "items": {"type": "string"}},  # Weaknesses or vulnerabilities
                "backstory": {"type": "array", "items": {"type": "string"}},  # Significant events from their past
                "symbolic_role": {"type": "array", "items": {"type": "string"}},  # What the character represents thematically
                "physical_description": {"type": "array", "items": {"type": "string"}},  # Appearance details
                'short_summary': {"type": "array", "items": {"type": "string"}},
                'long_summary': {"type": "array", "items": {"type": "string"}}
            },
            "required": [
                "role",
                "personality_traits",
                "motivations",
                "conflicts",
                "arc",
                "relationships",
                "strengths",
                "flaws",
                "backstory",
                'symbolic_role',
                'physical_description',
                'short_summary',
                'long_summary'
            ],
            "additionalProperties": False
        }
    }
}
