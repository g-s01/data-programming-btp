ABSTAIN = -1
O = 0
Person_OtherPER = 1
Person_Artist = 2
Group_SportsGRP = 3
Person_Athlete = 4
Group_ORG = 5
MEDICAL_MEDICATION_VACCINE = 6
MEDICAL_DISEASE = 7
Location_HumanSettlement = 8
Group_PublicCorp = 9
CreativeWorks_VisualWork = 10
Product_Vehicle = 11
Location_Facility = 12
Product_OtherPROD = 13
Person_Politician = 14
CreativeWorks_WrittenWork = 15
CreativeWorks_Software = 16
Location_OtherLOC = 17
Product_Food = 18
CreativeWorks_MusicalWork = 19
Person_Scientist = 20
Person_SportsManager = 21
Group_MusicalGroup = 22
Medical_AnatomicalStructure = 23
Product_Clothing = 24
Person_Cleric = 25
Medical_MedicalProcedure = 26
Location_Station = 27
Group_CarManufacturer = 28
Product_Drink = 29
Group_AeroSpaceManufacturer = 30
Medical_Symptom = 31
CreativeWorks_ArtWork = 32
Group_PrivateCorp = 33

def label_sentence_Person_OtherPER(tokens):
    """
    Labels each token in a sentence as Person_OtherPER if it is a person but not specifically classified as
    Scientist, Artist, Athlete, Politician, Cleric, or SportsManager. Otherwise, returns ABSTAIN.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # List of words commonly associated with specific person roles
    non_other_per_roles = {
        'scientist', 'artist', 'athlete', 'politician', 'cleric', 'sportsmanager'
    }
    
    # Contextual cues that indicate a person (e.g., titles, actions associated with people)
    person_indicators = {
        'mr', 'mrs', 'dr', 'professor', 'sir', 'lady', 'judge', 'founder', 'winner',
        'researcher', 'scholar', 'author', 'director'
    }

    labels = []
    
    for i, token in enumerate(tokens):
        token_lower = token.lower()
        
        # Check if the token is associated with a person based on context
        if (
            token_lower in person_indicators and  # Title indicating a person
            ((i > 0 and tokens[i - 1].lower() in person_indicators) or  # Preceded by a title
            (i < len(tokens) - 1 and tokens[i + 1].lower() in person_indicators))  # Followed by a title
        ):
            # Ensure the person is not in one of the more specific roles
            if (
                i < len(tokens) - 1 and tokens[i + 1].lower() not in non_other_per_roles and
                token_lower not in non_other_per_roles
            ):
                labels.append(Person_OtherPER)
            else:
                labels.append(ABSTAIN)
        else:
            labels.append(ABSTAIN) 

    return labels

def label_sentence_Person_SportsManager(tokens):
    """
    Labels each token in a sentence as Person-SportsManager if it indicates a person who is a sports manager.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Contextual words and titles related to sports managers
    sports_manager_titles = {
        'coach', 'head', 'manager', 'assistant', 'president', 'analyst'
    }
    sports_keywords = {
        'club', 'team', 'sports', 'football', 'basketball', 'university'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the current token is associated with a sports manager based on context
        if (
            token_lower in sports_manager_titles and (  # The token itself is a title
            (i > 0 and tokens[i - 1].lower() in sports_manager_titles) or  # Preceded by a sports title
            (i < len(tokens) - 1 and tokens[i + 1].lower() in sports_manager_titles)
            )  # Followed by a sports title
        ):
            # Ensure it is related to a sports context
            if (
                i > 0 and tokens[i - 1].lower() in sports_keywords or
                i < len(tokens) - 1 and tokens[i + 1].lower() in sports_keywords
            ):
                labels.append(Person_SportsManager)
            else:
                labels.append(ABSTAIN)
        else:
            labels.append(ABSTAIN)  # Default label if no match is found

    return labels

def label_sentence_Person_Cleric(tokens):
    """
    Labels each token in a sentence as Person-Cleric if it indicates a person associated with a clerical or religious role.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common religious titles and roles
    cleric_titles = {
        'pope', 'bishop', 'priest', 'archbishop', 'cardinal', 'pastor', 'reverend',
        'imam', 'rabbi', 'monk', 'friar', 'deacon', 'patriarch', 'cleric', 'provost'
    }
    religious_keywords = {
        'church', 'cathedral', 'parish', 'monastery', 'sanhedrin', 'faith', 'religion'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token matches known clerical titles
        if (
            token_lower in cleric_titles and  # The token itself is a clerical title
            ((i > 0 and tokens[i - 1].lower() in cleric_titles) or  # Preceded by a clerical title
            (i < len(tokens) - 1 and tokens[i + 1].lower() in cleric_titles))  # Followed by a clerical title
        ):
            labels.append(Person_Cleric)
        # Check if the context suggests a clerical role
        elif (
            (i > 0 and tokens[i - 1].lower() in religious_keywords) or
            (i < len(tokens) - 1 and tokens[i + 1].lower() in religious_keywords)
        ):
            labels.append(Person_Cleric)
        else:
            labels.append(ABSTAIN)  

    return labels

def label_sentence_Person_Politician(tokens):
    """
    Labels each token in a sentence as Person-Politician if it indicates a person associated with political roles.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common political titles and keywords
    politician_titles = {
        'president', 'prime', 'minister', 'chancellor', 'king', 'queen', 'governor', 'senator',
        'congressman', 'congresswoman', 'representative', 'delegate', 'councilor', 'ambassador',
        'mayor', 'monarch', 'tsar', 'emperor', 'leader', 'ruler'
    }
    political_keywords = {
        'government', 'political', 'administration', 'kingdom', 'empire', 'state', 'republic'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token matches known political titles
        if (
            token_lower in politician_titles and(  # The token itself is a political title
            (i > 0 and tokens[i - 1].lower() in politician_titles) or  # Preceded by a political title
            (i < len(tokens) - 1 and tokens[i + 1].lower() in politician_titles))  # Followed by a political title
        ):
            labels.append(Person_Politician)
        # Check if the context suggests a political role
        elif (
            (i > 0 and tokens[i - 1].lower() in political_keywords) or
            (i < len(tokens) - 1 and tokens[i + 1].lower() in political_keywords)
        ):
            labels.append(Person_Politician)
        else:
            labels.append(ABSTAIN) 

    return labels

def label_sentence_Person_Athelete(tokens):
    """
    Labels each token in a sentence as Person_Athlete if it indicates a person associated with sports or athletic roles.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common athlete-related terms and context keywords
    athlete_indicators = {
        'match', 'game', 'fight', 'race', 'tournament', 'champion', 'competition', 'player', 
        'runner', 'swimmer', 'fighter', 'athlete', 'coach', 'event'
    }
    sports_context = {
        'team', 'club', 'league', 'olympics', 'championship', 'tournament', 'event', 'middleweight',
        'kickboxer', 'commentator', 'announcer', 'season', 'series', 'round', 'final', 'medal',
        'training', 'court', 'field', 'stadium', 'pitch', 'arena', 'matchday', 'fixture', 'goal',
        'score', 'points', 'set', 'contest', 'semifinal', 'quarterfinal', 'athletics', 'sprint',
        'marathon', 'relay', 'triathlon', 'boxing', 'wrestling', 'MMA', 'karate', 'judo', 'taekwondo',
        'basketball', 'football', 'soccer', 'rugby', 'cricket', 'baseball', 'hockey', 'golf',
        'tennis', 'volleyball', 'badminton', 'skiing', 'skating', 'snowboarding', 'surfing'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an athlete
        if (
            token_lower in athlete_indicators and (  # The token itself indicates an athlete
            (i > 0 and tokens[i - 1].lower() in athlete_indicators) or  # Preceded by an indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in athlete_indicators) or  # Followed by an indicator
            (i > 0 and tokens[i - 1].lower() in sports_context) or  # Preceded by a sports context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in sports_context))  # Followed by a sports context keyword
        ):
            labels.append(Person_Athlete)
        else:
            labels.append(ABSTAIN)  

    return labels

def label_sentence_Person_Artist(tokens):
    """
    Labels each token in a sentence as Person-Artist if it indicates a person associated with artistic roles.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Expanded list of common artist-related terms and context keywords
    artist_indicators = {
        'painter', 'sculptor', 'musician', 'composer', 'singer', 'actor', 'actress', 'dancer',
        'performer', 'writer', 'author', 'director', 'producer', 'photographer', 'voice', 'voiced',
        'artist', 'poet', 'illustrator', 'choreographer', 'novelist', 'playwright', 'cinematographer',
        'filmmaker', 'editor', 'graphic', 'animator', 'designer', 'screenwriter', 'lyricist',
        'scenographer', 'conductor', 'orchestrator', 'arranger'
    }
    artistic_context = {
        'album', 'song', 'film', 'movie', 'theatre', 'play', 'performance', 'exhibition', 'art', 'gallery',
        'painting', 'sculpture', 'composition', 'novel', 'poem', 'story', 'design', 'show', 'series',
        'vocals', 'artwork', 'drawings', 'installations', 'opera', 'ballet', 'symphony', 'concerto',
        'mural', 'ceramics', 'pottery', 'dance', 'installation', 'multimedia', 'short', 'animation',
        'soundtrack', 'score', 'music', 'stage', 'choreography', 'set', 'costume', 'fashion'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()
        # Check if the token or surrounding tokens suggest an artist
        if (
            token_lower in artist_indicators and (  # The token itself indicates an artist role
            (i > 0 and tokens[i - 1].lower() in artist_indicators) or  # Preceded by an artist role
            (i < len(tokens) - 1 and tokens[i + 1].lower() in artist_indicators) or  # Followed by an artist role
            (i > 0 and tokens[i - 1].lower() in artistic_context) or  # Preceded by an artistic context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in artistic_context))  # Followed by an artistic context keyword
        ):
            labels.append(Person_Artist)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Person_Scientist(tokens):
    """
    Labels each token in a sentence as Person-Scientist if it indicates a person associated with scientific roles.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common scientist-related terms and context keywords
    scientist_indicators = {
        'scientist', 'professor', 'researcher', 'physicist', 'chemist', 'biologist', 'mathematician',
        'geologist', 'astronomer', 'engineer', 'inventor', 'theorist', 'anthropologist', 'sociologist',
        'psychologist', 'economist', 'philosopher', 'archaeologist'
    }
    scientific_context = {
        'research', 'experiment', 'study', 'theory', 'discovery', 'analysis', 'article', 'paper',
        'journal', 'work', 'science', 'mathematics', 'engineering', 'biology', 'chemistry', 'physics',
        'pioneering', 'project', 'professors', 'vaccination', 'invention', 'technology', 'innovation',
        'publication', 'society', 'conference', 'institute', 'university', 'academic', 'field', 'practice'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a scientist
        if (
            token_lower in scientist_indicators and (  # The token itself indicates a scientist role
            (i > 0 and tokens[i - 1].lower() in scientist_indicators) or  # Preceded by a scientist role
            (i < len(tokens) - 1 and tokens[i + 1].lower() in scientist_indicators) or  # Followed by a scientist role
            (i > 0 and tokens[i - 1].lower() in scientific_context) or  # Preceded by a scientific context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in scientific_context))  # Followed by a scientific context keyword
        ):
            labels.append(Person_Scientist)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Medical_Disease(tokens):
    """
    Labels each token in a sentence as Medical_Disease if it indicates a medical disease or condition.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common disease-related terms and context keywords
    disease_indicators = {
        'disease', 'syndrome', 'disorder', 'condition', 'illness', 'fever', 'cancer', 'infection',
        'defect', 'paralysis', 'delusion', 'malady', 'ailment', 'affliction'
    }
    medical_context = {
        'diagnosed', 'treated', 'symptoms', 'remedy', 'therapy', 'treatment', 'medication',
        'caused', 'risk', 'factors', 'condition', 'autoimmune', 'genetic', 'psychiatric',
        'mental', 'chronic', 'acute', 'infection', 'virus', 'disease', 'outbreak', 'epidemic',
        'pandemic', 'epileptic', 'drug', 'medications', 'response', 'clinical'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a disease
        if (
            token_lower in disease_indicators and (  # The token itself indicates a disease
            (i > 0 and tokens[i - 1].lower() in disease_indicators) or  # Preceded by a disease indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in disease_indicators) or  # Followed by a disease indicator
            (i > 0 and tokens[i - 1].lower() in medical_context) or  # Preceded by a medical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_context))  # Followed by a medical context keyword
        ):
            labels.append(MEDICAL_DISEASE)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Medical_Symptom(tokens):
    """
    Labels each token in a sentence as Medical_Symptom if it indicates a medical symptom or related condition.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common symptom-related terms and context keywords
    symptom_indicators = {
        'pain', 'fatigue', 'nausea', 'drowsiness', 'vomiting', 'cough', 'anxiety', 'insomnia',
        'swelling', 'shortness', 'breath', 'twitching', 'sputum', 'dysphoric', 'mood', 'pseudovaginal',
        'deafness', 'sweating', 'fever', 'chills', 'headache', 'itching', 'rash', 'weakness', 'dizziness',
        'soreness', 'paralysis', 'discomfort', 'agitation', 'cramps', 'bleeding', 'blurry', 'vision',
        'cramping', 'inflammation'
    }
    medical_context = {
        'diagnosed', 'treat', 'remedy', 'therapy', 'condition', 'chronic', 'acute', 'symptoms', 'caused',
        'managed', 'treated', 'signs', 'associated', 'relieved', 'painful', 'present', 'episodes', 'attack'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a symptom
        if (
            token_lower in symptom_indicators and (  # The token itself indicates a symptom
            (i > 0 and tokens[i - 1].lower() in symptom_indicators) or  # Preceded by a symptom indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in symptom_indicators) or  # Followed by a symptom indicator
            (i > 0 and tokens[i - 1].lower() in medical_context) or  # Preceded by a medical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_context))  # Followed by a medical context keyword
        ):
            labels.append(Medical_Symptom)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Medical_AnatomicalStructure(tokens):
    """
    Labels each token in a sentence as Medical_AnatomicalStructure if it indicates a body part or anatomical structure.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common anatomical structures and body parts
    anatomical_indicators = {
        'heart', 'brain', 'hippocampus', 'cerebellum', 'atrium', 'ventricle', 'vein', 'artery',
        'nervous', 'system', 'tissue', 'muscle', 'bone', 'joint', 'ligament', 'tendon', 'organ',
        'lung', 'kidney', 'liver', 'skin', 'spine', 'spinal', 'cord', 'cranial', 'ridges',
        'glands', 'node', 'atrioventricular', 'connective', 'membrane', 'stomach', 'intestine',
        'colon', 'spleen', 'pancreas', 'esophagus', 'trachea', 'bronchi', 'rib', 'sternum', 'pelvis',
        'scalp', 'retina', 'cornea', 'pupil', 'iris', 'ear', 'cochlea', 'larynx', 'pharynx', 'epidermis',
        'bone marrow', 'cartilage', 'parietal', 'temporal', 'occipital', 'frontal', 'ulna', 'radius',
        'fibula', 'tibia', 'femur', 'humerus'
    }
    medical_context = {
        'located', 'surrounding', 'structure', 'play', 'role', 'function', 'related', 'maintains',
        'part', 'involved', 'consolidation', 'growth', 'support', 'protects', 'linked', 'connected'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an anatomical structure
        if (
            token_lower in anatomical_indicators and (  # The token itself indicates an anatomical structure
            (i > 0 and tokens[i - 1].lower() in anatomical_indicators) or  # Preceded by an anatomical indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in anatomical_indicators) or  # Followed by an anatomical indicator
            (i > 0 and tokens[i - 1].lower() in medical_context) or  # Preceded by a medical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_context))  # Followed by a medical context keyword
        ):
            labels.append(Medical_AnatomicalStructure)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Medical_Medical_Procedure(tokens):
    """
    Labels each token in a sentence as Medical_MedicalProcedure if it indicates a medical procedure or treatment.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common medical procedures and related terms
    medical_procedure_indicators = {
        'surgery', 'chemotherapy', 'radiation', 'vaccination', 'therapy', 'treatment', 'operation',
        'amputation', 'hysterectomy', 'transplant', 'biopsy', 'ventilation', 'procedure', 'dialysis',
        'catheterization', 'intubation', 'injection', 'infusion', 'transfusion', 'test', 'scanning',
        'x-ray', 'ultrasound', 'mri', 'ct', 'procedure', 'implantation', 'stenting', 'bypass'
    }
    medical_context = {
        'performed', 'conducted', 'administered', 'treated', 'underwent', 'requires', 'needed',
        'developed', 'pioneered', 'prescribed', 'recommended', 'therapy', 'response', 'outcome',
        'test', 'positive', 'negative', 'evaluation', 'session', 'treatment'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a medical procedure
        if (
            token_lower in medical_procedure_indicators and (  # The token itself indicates a medical procedure
            (i > 0 and tokens[i - 1].lower() in medical_procedure_indicators) or  # Preceded by a procedure indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_procedure_indicators) or  # Followed by a procedure indicator
            (i > 0 and tokens[i - 1].lower() in medical_context) or  # Preceded by a medical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_context))  # Followed by a medical context keyword
        ):
            labels.append(Medical_MedicalProcedure)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Medical_Medication_Vaccince(tokens):
    """
    Labels each token in a sentence as Medical-Medication/Vaccine if it indicates a medical drug or vaccine.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common medication and vaccine indicators
    medication_vaccine_indicators = {
        'azidothymidine', 'azt', 'atomoxetine', 'norepinephrine', 'letrozole', 'misoprostol',
        'dextromethorphan', 'quinine', 'hormone', 'drug', 'medication', 'vaccine', 'antibiotic',
        'antiviral', 'antifungal', 'steroid', 'analgesic', 'antidepressant', 'antihistamine',
        'chemotherapy', 'immunization', 'inhibitor', 'suspension', 'tablet', 'capsule', 'injection',
        'serum', 'antibody', 'booster', 'shot'
    }
    medical_context = {
        'prescribed', 'taken', 'administered', 'treat', 'treatment', 'therapy', 'dose', 'injection',
        'prevent', 'used', 'preventative', 'response', 'combination', 'available', 'pharmaceutical',
        'therapy', 'medicinal', 'over-the-counter'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest medication or a vaccine
        if (
            token_lower in medication_vaccine_indicators and ( # The token itself indicates a medication or vaccine
            (i > 0 and tokens[i - 1].lower() in medication_vaccine_indicators) or  # Preceded by a medication indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medication_vaccine_indicators) or  # Followed by a medication indicator
            (i > 0 and tokens[i - 1].lower() in medical_context) or  # Preceded by a medical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in medical_context))  # Followed by a medical context keyword
        ):
            labels.append(MEDICAL_MEDICATION_VACCINE)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Product_OtherPROD(tokens):
    """
    Labels each token in a sentence as Product_OtherPROD if it indicates a product not classified under specific categories.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common product indicators
    other_prod_indicators = {
        'polygraph', 'phonograph', 'cylinder', 'drums', 'guitar', 'keyboards', 'piano', 'organ',
        'wurlitzer', 'shaker', 'tambourine', 'production', 'mixing', 'recording', 'bass', 'percussion',
        'track', 'vocals'
    }
    product_context = {
        'manufactured', 'built', 'produced', 'designed', 'created', 'featured', 'developed',
        'product', 'equipment', 'device', 'instrument', 'gear', 'model', 'system', 'technology'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a product
        if (
            token_lower in other_prod_indicators and (  # The token itself indicates a product
            (i > 0 and tokens[i - 1].lower() in other_prod_indicators) or  # Preceded by a product indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in other_prod_indicators) or  # Followed by a product indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a product context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a product context keyword
        ):
            labels.append(Product_OtherPROD)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Product_Drink(tokens):
    """
    Labels each token in a sentence as Product_Drink if it indicates a type of drink or beverage.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common drink-related indicators
    drink_indicators = {
        'water', 'prosecco', 'coca-cola', 'apfelkorn', 'liqueur', 'coffee', 'milk', 'wine',
        'postum', 'beverage', 'juice', 'tea', 'soda', 'cider', 'beer', 'cocktail', 'spirit',
        'champagne', 'smoothie', 'latte', 'espresso', 'mocha', 'tonic', 'lemonade', 'milkshake',
        'whiskey', 'vodka', 'rum', 'gin', 'brandy', 'liqueur', 'sake', 'kombucha', 'matcha', 
        'chai', 'herbal', 'infusion', 'alcoholic', 'punch'
    }
    product_context = {
        'served', 'drank', 'consumed', 'beverage', 'drink', 'poured', 'accompanied', 'with',
        'glass', 'shot', 'cup', 'bottle', 'flask', 'tumbler', 'refreshing', 'sweetened'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a drink
        if (
            token_lower in drink_indicators and (  # The token itself indicates a drink
            (i > 0 and tokens[i - 1].lower() in drink_indicators) or  # Preceded by a drink indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in drink_indicators) or  # Followed by a drink indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a drink context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a drink context keyword
        ):
            labels.append(Product_Drink)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Product_Food(tokens):
    """
    Labels each token in a sentence as Product-Food if it indicates a type of food or food product.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common food-related indicators
    food_indicators = {
        'pastry', 'cocoa', 'beans', 'noodles', 'salt', 'sugar', 'vinegar', 'yeast', 'ingredient',
        'sauce', 'acetic', 'acid', 'vinegar', 'instant', 'cup', 'posca', 'wine', 'ethanol', 'syrup',
        'bread', 'cheese', 'fruit', 'vegetable', 'meat', 'honey', 'spice', 'herb', 'rice', 'grain',
        'flour', 'pasta', 'oil', 'butter', 'milk', 'cream', 'yogurt', 'nuts', 'almonds', 'cashews',
        'walnuts', 'coconut', 'egg', 'chocolate', 'candy', 'snack', 'meal', 'dish'
    }
    product_context = {
        'prepared', 'cooked', 'eaten', 'served', 'ingredient', 'dish', 'food', 'meal', 'recipe',
        'cuisine', 'taste', 'flavor', 'baked', 'fried', 'boiled', 'grilled', 'roasted'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest food
        if (
            token_lower in food_indicators and (  # The token itself indicates food
            (i > 0 and tokens[i - 1].lower() in food_indicators) or  # Preceded by a food indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in food_indicators) or  # Followed by a food indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a food context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a food context keyword
        ):
            labels.append(Product_Food)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Product_Vehicle(tokens):
    """
    Labels each token in a sentence as Product_Vehicle if it indicates a type of vehicle or transportation product.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common vehicle-related indicators
    vehicle_indicators = {
        'car', 'train', 'locomotive', 'ship', 'boat', 'sailing', 'vessel', 'aircraft', 'plane', 'helicopter',
        'submarine', 'yacht', 'whaler', 'junk', 'tram', 'bus', 'bicycle', 'motorcycle', 'scooter', 'sedan',
        'coupe', 'convertible', 'truck', 'lorry', 'jeep', 'tractor', 'ambulance', 'van', 'wagon', 'cab',
        'd-type', 'express', 'carrier', 'steamer'
    }
    product_context = {
        'driving', 'built', 'operating', 'commissioned', 'sailed', 'launched', 'model', 'fitted', 'equipped',
        'vehicle', 'transport', 'engine', 'design', 'expedition', 'route', 'journey', 'trip'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a vehicle
        if (
            token_lower in vehicle_indicators and (  # The token itself indicates a vehicle
            (i > 0 and tokens[i - 1].lower() in vehicle_indicators) or  # Preceded by a vehicle indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in vehicle_indicators) or  # Followed by a vehicle indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a vehicle context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a vehicle context keyword
        ):
            labels.append(Product_Vehicle)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Product_Clothing(tokens):
    """
    Labels each token in a sentence as Product_Clothing if it indicates a type of clothing or apparel.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common clothing-related indicators
    clothing_indicators = {
        'shirt', 'jumper', 'skirt', 'trousers', 'bikini', 'sarong', 'garments', 'robe', 'turban',
        'caps', 'jacket', 'coat', 'dress', 'pants', 'sweater', 'scarf', 'gloves', 'hat', 'suit',
        'tie', 'gown', 'uniform', 'tunic', 'costume', 'blouse', 'jeans', 'shorts', 'leggings',
        'hoodie', 'socks', 'shoes', 'boots', 'sandals', 'slippers', 'swimwear', 'sheath', 'tefillin'
    }
    product_context = {
        'wearing', 'dressed', 'donning', 'wore', 'fashion', 'apparel', 'clothes', 'outfit', 'tailored',
        'traditional', 'designed', 'attire', 'fabric', 'woven', 'pattern', 'sewn'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest clothing
        if (
            token_lower in clothing_indicators and (  # The token itself indicates clothing
            (i > 0 and tokens[i - 1].lower() in clothing_indicators) or  # Preceded by a clothing indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in clothing_indicators) or  # Followed by a clothing indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a clothing context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a clothing context keyword
        ):
            labels.append(Product_Clothing)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_ORG(tokens):
    """
    Labels each token in a sentence as Group-ORG if it indicates an organization.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common organization indicators
    org_indicators = {
        'academy', 'award', 'party', 'army', 'faction', 'empire', 'chain', 'association',
        'store', 'hotels', 'company', 'university', 'corporation', 'union', 'federation',
        'institute', 'congress', 'committee', 'council', 'league', 'organization', 'firm',
        'department', 'agency', 'group', 'bank', 'charity', 'foundation'
    }
    org_context = {
        'founded', 'led', 'association', 'member', 'board', 'president', 'ceo', 'vice',
        'chairman', 'founder', 'headquarters', 'offices', 'division', 'subsidiary', 'affiliate',
        'branch', 'partner', 'alliance'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an organization
        if (
            token_lower in org_indicators and ( # The token itself indicates an organization
            (i > 0 and tokens[i - 1].lower() in org_indicators) or  # Preceded by an organization indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in org_indicators) or  # Followed by an organization indicator
            (i > 0 and tokens[i - 1].lower() in org_context) or  # Preceded by an organization context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in org_context))  # Followed by an organization context keyword
        ):
            labels.append(Group_ORG)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_CarManufacturer(tokens):
    """
    Labels each token in a sentence as Group_CarManufacturer if it indicates a car manufacturer or automotive brand.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common car manufacturer indicators
    car_manufacturer_indicators = {
        'toyota', 'subaru', 'mitsubishi', 'suzuki', 'ferrari', 'mclaren', 'ford', 'lexus',
        'holden', 'avtoframos', 'dkw', 'triumph', 'honda', 'nissan', 'chevrolet', 'bmw',
        'audi', 'mercedes', 'volkswagen', 'volvo', 'jaguar', 'porsche', 'tesla', 'renault',
        'peugeot', 'mazda', 'kia', 'hyundai', 'alfa', 'romeo', 'bugatti', 'aston', 'martin',
        'lamborghini', 'bentley', 'rolls-royce', 'fiat'
    }
    product_context = {
        'manufactured', 'produced', 'built', 'brand', 'model', 'car', 'automotive', 'team', 'race', 
        'driven', 'driving', 'vehicle', 'maker', 'factory', 'plant'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a car manufacturer
        if (
            token_lower in car_manufacturer_indicators and (  # The token itself indicates a car manufacturer
            (i > 0 and tokens[i - 1].lower() in car_manufacturer_indicators) or  # Preceded by a car manufacturer
            (i < len(tokens) - 1 and tokens[i + 1].lower() in car_manufacturer_indicators) or  # Followed by a car manufacturer
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a car context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a car context keyword
        ):
            labels.append(Group_CarManufacturer)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_SportsGRP(tokens):
    """
    Labels each token in a sentence as Group_SportsGRP if it indicates a sports group, team, or organization.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common sports group indicators
    sports_grp_indicators = {
        'team', 'club', 'gaa', 'university', 'association', 'league', 'squad', 'side',
        'fc', 'hc', 'ac', 'rc', 'athletic', 'olympians', 'batsman', 'goalkeeper', 'medal',
        'gold', 'cricket', 'rugby', 'soccer', 'hockey', 'basketball', 'baseball'
    }
    sports_teams = {
        'essex', 'multan', 'west', 'tokyo', 'all', 'kilkenny', 'tyrone', 'hungary', 'poland'
    }
    sports_context = {
        'match', 'game', 'tournament', 'championship', 'cup', 'medal', 'season', 'stage',
        'played', 'winner', 'won', 'lost', 'scored', 'points', 'final', 'relegation', 'recruited',
        'signed', 'manager', 'coach'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a sports group
        if (
            token_lower in sports_grp_indicators and (  # The token itself indicates a sports group
            token_lower in sports_teams or  # Specific team names
            (i > 0 and tokens[i - 1].lower() in sports_grp_indicators) or  # Preceded by a sports group indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in sports_grp_indicators) or  # Followed by a sports group indicator
            (i > 0 and tokens[i - 1].lower() in sports_context) or  # Preceded by a sports context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in sports_context))  # Followed by a sports context keyword
        ):
            labels.append(Group_SportsGRP)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_AerospaceManufacturer(tokens):
    """
    Labels each token in a sentence as Group_AerospaceManufacturer if it indicates an aerospace manufacturing company or group.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common aerospace manufacturer indicators
    aerospace_indicators = {
        'boeing', 'airbus', 'lockheed', 'martin', 'northrop', 'grumman', 'raytheon', 'general',
        'dynamics', 'north', 'american', 'aviation', 'united', 'helicopters', 'british', 'aerospace',
        'siemens', 'halske', 'nakajima', 'hitachi', 's.e.saunders', 'cowes'
    }
    product_context = {
        'aerospace', 'aircraft', 'helicopter', 'plane', 'jet', 'manufactured', 'produced', 'engine',
        'works', 'designed', 'built', 'technology', 'group', 'company', 'corporation', 'engineer',
        'pilot', 'test', 'system', 'signals'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an aerospace manufacturer
        if (
            token_lower in aerospace_indicators and (  # The token itself indicates an aerospace manufacturer
            (i > 0 and tokens[i - 1].lower() in aerospace_indicators) or  # Preceded by an aerospace manufacturer indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in aerospace_indicators) or  # Followed by an aerospace manufacturer indicator
            (i > 0 and tokens[i - 1].lower() in product_context) or  # Preceded by a product context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in product_context))  # Followed by a product context keyword
        ):
            labels.append(Group_AeroSpaceManufacturer)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_CreativeWorks_Software(tokens):
    """
    Labels each token in a sentence as CreativeWorks_Software if it indicates a software product, program, or video game.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    software_indicators = {
        'hypertext', 'lego', 'batman', 'dc', 'super', 'heroes', 'resident', 'evil', 'nemesis',
        'mario', 'mycroft', 'infocom', 'sherlock', 'hes', 'excel', 'photoshop', 'word',
        'powerpoint', 'autocad', 'blender', 'gimp', 'slack', 'notepad++', 'vim', 'sublime',
        'atom', 'mysql', 'postgresql', 'oracle', 'firefox', 'chrome', 'safari', 'internet',
        'explorer', 'outlook', 'thunderbird', 'skype', 'teams', 'zoom', 'discord', 'trello',
        'asana', 'jira', 'confluence', 'unity', 'unreal', 'godot', 'tiktok', 'snapchat'
    }
    software_context = {
        'game', 'program', 'app', 'application', 'software', 'tool', 'platform', 'developed',
        'released', 'published', 'version', 'update', 'patch', 'module'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest software
        if (
            token_lower in software_indicators and (  # The token itself indicates software
#            token_lower in software_names or  # Specific software names
            (i > 0 and tokens[i - 1].lower() in software_indicators) or  # Preceded by a software indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in software_indicators) or  # Followed by a software indicator
            (i > 0 and tokens[i - 1].lower() in software_context) or  # Preceded by a software context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in software_context))  # Followed by a software context keyword
        ):
            labels.append(CreativeWorks_Software)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_CreativeWorks_ArtWork(tokens):
    """
    Labels each token in a sentence as CreativeWorks_ArtWork if it indicates a work of art such as a painting, sculpture, or visual piece.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common artwork-related indicators
    artwork_indicators = {
        'painting', 'sculpture', 'portrait', 'masterpiece', 'miniature', 'canvas', 'oil', 'watercolour',
        'etching', 'drawing', 'sketch', 'mural', 'fresco', 'illustration', 'print', 'sculpted', 'monument',
        'bust', 'statue', 'relief', 'installation'
    }
    artwork_titles = {
        'atelier', 'rouge', 'threatened', 'swan', 'agnew', 'clinic', 'tarquin', 'lucretia'
    }
    artwork_context = {
        'painted', 'sculpted', 'created', 'depicted', 'portrayed', 'featured', 'museum', 'exhibition',
        'collection', 'gallery', 'display', 'shown', 'masterpiece', 'work', 'art', 'visual', 'piece'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an artwork
        if (
            token_lower in artwork_indicators and (  # The token itself indicates an artwork
            token_lower in artwork_titles or  # Specific artwork titles
            (i > 0 and tokens[i - 1].lower() in artwork_indicators) or  # Preceded by an artwork indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in artwork_indicators) or  # Followed by an artwork indicator
            (i > 0 and tokens[i - 1].lower() in artwork_context) or  # Preceded by an artwork context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in artwork_context))  # Followed by an artwork context keyword
        ):
            labels.append(CreativeWorks_ArtWork)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_CreativeWorks_WrittenWork(tokens):
    """
    Labels each token in a sentence as CreativeWorks_WrittenWork if it indicates a written work such as a book, article, or manuscript.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common written work indicators
    written_work_indicators = {
        'book', 'article', 'document', 'novel', 'manuscript', 'story', 'poem', 'series',
        'publication', 'journal', 'editor', 'anthology', 'text', 'script', 'treatise',
        'essay', 'volume', 'biography', 'memoir', 'documentary', 'chronicle', 'saga', 'play'
    }
    written_work_titles = {
        'fanshen', 'dionysiaca', 'ruby', 'smoke', 'sally', 'lockhart'
    }
    written_work_context = {
        'written', 'described', 'documented', 'authored', 'translated', 'published', 'co-author',
        'editor', 'revised', 'edition', 'series', 'translated', 'published', 'chapter', 'book',
        'works', 'writing', 'systems', 'story', 'based', 'on', 'fictional'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a written work
        if (
            token_lower in written_work_indicators and (  # The token itself indicates a written work
            token_lower in written_work_titles or  # Specific written work titles
            (i > 0 and tokens[i - 1].lower() in written_work_indicators) or  # Preceded by a written work indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in written_work_indicators) or  # Followed by a written work indicator
            (i > 0 and tokens[i - 1].lower() in written_work_context) or  # Preceded by a written work context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in written_work_context))  # Followed by a written work context keyword
        ):
            labels.append(CreativeWorks_WrittenWork)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_CreativeWorks_MusicalWork(tokens):
    """
    Labels each token in a sentence as CreativeWorks_MusicalWork if it indicates a musical work such as a song, composition, or musical piece.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common musical work indicators
    musical_work_titles = {
        'song', 'album', 'composition', 'concerto', 'opera', 'symphony', 'cantata', 'sonata',
        'ballad', 'anthem', 'aria', 'suite', 'overture', 'march', 'nocturne', 'waltz', 'rhapsody',
        'scherzo', 'fugue', 'prelude', 'toccata', 'fantasia', 'carol', 'melody', 'tune', 'score',
        'piece', 'chorale', 'oratorio', 'track'
    }
    musical_work_indicators = {
        'vocals', 'lyrics', 'album', 'track', 'composition', 'song', 'anthem', 'aria', 'march',
        'nocturne', 'overture', 'suite', 'symphony', 'ballad', 'piece', 'melody', 'chorale', 'score',
        'opera', 'cantata', 'concert', 'music', 'recording', 'version', 'oratorio', 'prelude'
    }
    musical_context = {
        'written', 'performed', 'sings', 'composed', 'featuring', 'includes', 'from', 'in', 'recorded',
        'covered', 'released', 'soundtrack', 'album', 'single', 'track'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a musical work
        if (
            token_lower in musical_work_indicators and (  # The token itself indicates a musical work
            token_lower in musical_work_titles or  # Specific musical work titles
            (i > 0 and tokens[i - 1].lower() in musical_work_indicators) or  # Preceded by a musical work indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in musical_work_indicators) or  # Followed by a musical work indicator
            (i > 0 and tokens[i - 1].lower() in musical_context) or  # Preceded by a musical context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in musical_context))  # Followed by a musical context keyword
        ):
            labels.append(CreativeWorks_MusicalWork)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_CreativeWorks_VisualWork(tokens):
    """
    Labels each token in a sentence as CreativeWorks_VisualWork if it indicates a visual work such as a film, TV series, or visual media.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common visual work indicators
    visual_work_titles = {
        'film', 'movie', 'show', 'series', 'episode', 'documentary', 'animation', 'cartoon',
        'drama', 'sitcom', 'miniseries', 'special', 'feature', 'broadcast', 'clip', 'segment',
        'presentation', 'program', 'television', 'cinema', 'picture', 'trailer', 'screenplay',
        'adaptation', 'biopic', 'production', 'episode', 'story', 'play', 'performance', 'skit',
        'short', 'commercial', 'broadcast', 'video', 'scene'
    }
    visual_work_indicators = {
        'art', 'direction', 'show', 'film', 'movie', 'series', 'television', 'documentary',
        'production', 'program', 'feature', 'performance', 'screen', 'animation', 'episode',
        'special', 'broadcast', 'clip', 'scene', 'play', 'adaptation', 'biopic', 'picture'
    }
    visual_context = {
        'released', 'aired', 'starring', 'featuring', 'broadcasted', 'produced', 'directed',
        'acted', 'co-anchored', 'cast', 'remade', 'screened', 'presented'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a visual work
        if (
            token_lower in visual_work_indicators and (  # The token itself indicates a visual work
            token_lower in visual_work_titles or  # Specific visual work titles
            (i > 0 and tokens[i - 1].lower() in visual_work_indicators) or  # Preceded by a visual work indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in visual_work_indicators) or  # Followed by a visual work indicator
            (i > 0 and tokens[i - 1].lower() in visual_context) or  # Preceded by a visual context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in visual_context))  # Followed by a visual context keyword
        ):
            labels.append(CreativeWorks_VisualWork)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Location_Station(tokens):
    """
    Labels each token in a sentence as Location_Station if it indicates a station or transit hub.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common station indicators
    station_names = {
        'station', 'terminus', 'platform', 'depot', 'junction', 'hub', 'terminal', 'interchange',
        'bay', 'halt', 'stop', 'yard', 'subway', 'metro', 'express', 'branch', 'railway', 'track',
        'pier', 'loop', 'crossing', 'depot', 'port'
    }
    station_indicators = {
        'station', 'terminal', 'stop', 'depot', 'platform', 'track', 'yard', 'junction', 'hub',
        'express', 'route', 'pier', 'crossing', 'subway', 'metro'
    }
    station_context = {
        'served', 'located', 'construction', 'branch', 'line', 'connected', 'route', 'service',
        'built', 'used', 'transit', 'rail', 'transportation', 'trains', 'operating', 'near'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a station
        if (
            token_lower in station_indicators and (  # The token itself indicates a station
            token_lower in station_names or  # Specific station names
            (i > 0 and tokens[i - 1].lower() in station_indicators) or  # Preceded by a station indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in station_indicators) or  # Followed by a station indicator
            (i > 0 and tokens[i - 1].lower() in station_context) or  # Preceded by a station context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in station_context))  # Followed by a station context keyword
        ):
            labels.append(Location_Station)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Location_HumanSettlement(tokens):
    """
    Labels each token in a sentence as Location_HumanSettlement if it indicates a city, town, or settlement.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common human settlement indicators
    settlement_indicators = {
        'city', 'town', 'village', 'settlement', 'hamlet', 'metropolis', 'municipality', 'capital'
    }
    known_settlement_names = {
        'kraków', 'paris', 'jamshedpur', 'philadelphia', 'manila', 'spain', 'india', 'china', 'turkmenistan'
    }
    settlement_context = {
        'born', 'went', 'moved', 'lived', 'visited', 'studied', 'traveled', 'resided', 'known', 'from', 'to'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a human settlement
        if (
            token_lower in settlement_indicators and (  # The token itself indicates a settlement
            token_lower in known_settlement_names or  # Specific known settlement names
            (i > 0 and tokens[i - 1].lower() in settlement_indicators) or  # Preceded by a settlement indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in settlement_indicators) or  # Followed by a settlement indicator
            (i > 0 and tokens[i - 1].lower() in settlement_context) or  # Preceded by a settlement context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in settlement_context))  # Followed by a settlement context keyword
        ):
            labels.append(Location_HumanSettlement)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Location_OtherLOC(tokens):
    """
    Labels each token in a sentence as Location_OtherLOC if it indicates a landmark, museum, or non-settlement location.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common other location indicators
    other_loc_indicators = {
        'museum', 'park', 'hall', 'road', 'headquarters', 'department', 'monument', 'bridge', 'tower',
        'arc', 'square', 'site', 'center', 'building', 'structure', 'complex'
    }
    known_other_loc_names = {
        'arc', 'triomphe', 'reuters', 'american', 'natural', 'history', 'please', 'touch', 'ministry', 'defense'
    }
    other_loc_context = {
        'located', 'situated', 'famous', 'holds', 'houses', 'known', 'ran', 'operates', 'next', 'near',
        'built', 'constructed', 'dedicated', 'memorial', 'landmark'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest an other location
        if (
            token_lower in other_loc_indicators and (  # The token itself indicates a non-settlement location
            token_lower in known_other_loc_names or  # Specific non-settlement location names
            (i > 0 and tokens[i - 1].lower() in other_loc_indicators) or  # Preceded by a non-settlement location indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in other_loc_indicators) or  # Followed by a non-settlement location indicator
            (i > 0 and tokens[i - 1].lower() in other_loc_context) or  # Preceded by a non-settlement location context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in other_loc_context))  # Followed by a non-settlement location context keyword
        ):
            labels.append(Location_OtherLOC)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Location_Facility(tokens):
    """
    Labels each token in a sentence as Location_Facility if it indicates a building, institution, or facility.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common facility-related indicators
    facility_indicators = {
        'museum', 'tower', 'hall', 'observatory', 'center', 'gallery', 'stadium', 'arena', 'hospital',
        'clinic', 'library', 'school', 'college', 'university', 'theater', 'cinema', 'office', 'studio'
    }
    known_facility_names = {
        'british', 'greenwich', 'hill–stead', 'kingsley', 'coit'
    }
    facility_context = {
        'worked', 'built', 'founded', 'designed', 'constructed', 'located', 'responsible', 'facility', 'exhibition',
        'headquarters', 'operates', 'ran', 'purchases', 'houses'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a facility
        if (
            token_lower in facility_indicators and (  # The token itself indicates a facility
            token_lower in known_facility_names or  # Specific facility names
            (i > 0 and tokens[i - 1].lower() in facility_indicators) or  # Preceded by a facility indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in facility_indicators) or  # Followed by a facility indicator
            (i > 0 and tokens[i - 1].lower() in facility_context) or  # Preceded by a facility context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in facility_context))  # Followed by a facility context keyword
        ):
            labels.append(Location_Facility)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_PrivateCorp(tokens):
    """
    Labels each token in a sentence as Group_PrivateCorp if it indicates a private corporation or company.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common private corporation indicators
    private_corp_indicators = {
        'gmbh', 'aps', 'bv', 'ltd', 'llc', 'inc', 'corporation', 'company', 'firm', 'group',
        'enterprise', 'studio', 'agency', 'solutions', 'partners'
    }
    known_private_corp_names = {
        'hallmark', 'glassesusa', 'trinity', 'apm', 'ivanhoé', 'cambridge', 'pbsc', 'domtar',
        'georgia-pacific', 'khaadi'
    }
    private_corp_context = {
        'founded', 'launched', 'owned', 'produced', 'supplied', 'managed', 'operated', 'converted',
        'merged', 'headquarters', 'subsidiary', 'division', 'brand', 'partnered', 'collaboration'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a private corporation
        if (
            token_lower in private_corp_indicators and (  # The token itself indicates a private corporation
            token_lower in known_private_corp_names or  # Specific private corporation names
            (i > 0 and tokens[i - 1].lower() in private_corp_indicators) or  # Preceded by a private corporation indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in private_corp_indicators) or  # Followed by a private corporation indicator
            (i > 0 and tokens[i - 1].lower() in private_corp_context) or  # Preceded by a private corporation context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in private_corp_context))  # Followed by a private corporation context keyword
        ):
            labels.append(Group_PrivateCorp)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Group_PublicCorp(tokens):
    """
    Labels each token in a sentence as Group_PublicCorp if it indicates a publicly traded corporation or large company.
    Returns ABSTAIN for tokens that do not match the category.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of labels for each token.
    """
    # Common public corporation indicators
    public_corp_indicators = {
        'corporation', 'company', 'inc', 'ltd', 'plc', 'group', 'corp', 'enterprise', 'holdings'
    }
    known_public_corp_names = {
        'ecopetrol', 'john', 'deere', 'jr', 'east', 'oricon', 'cumulus', 'media', 'vf', 'disney',
        'commonwealth', 'banking', 'ping', 'insurance', 'costco', 'hewlett-packard', 'marks',
        'spencer', 'morgan', 'stanley'
    }
    public_corp_context = {
        'owned', 'operated', 'managed', 'produced', 'purchased', 'expanded', 'founded', 'acquired',
        'appointed', 'brand', 'partner', 'served', 'listed', 'stock', 'traded', 'shares', 'subsidiary'
    }

    labels = []

    for i, token in enumerate(tokens):
        token_lower = token.lower()

        # Check if the token or surrounding tokens suggest a public corporation
        if (
            token_lower in public_corp_indicators and (  # The token itself indicates a public corporation
            token_lower in known_public_corp_names or  # Specific public corporation names
            (i > 0 and tokens[i - 1].lower() in public_corp_indicators) or  # Preceded by a public corporation indicator
            (i < len(tokens) - 1 and tokens[i + 1].lower() in public_corp_indicators) or  # Followed by a public corporation indicator
            (i > 0 and tokens[i - 1].lower() in public_corp_context) or  # Preceded by a public corporation context keyword
            (i < len(tokens) - 1 and tokens[i + 1].lower() in public_corp_context))  # Followed by a public corporation context keyword
        ):
            labels.append(Group_PublicCorp)
        else:
            labels.append(ABSTAIN)  # Default to 'O' if no match is found

    return labels

def label_sentence_Location_Person(tokens):
    """
    Labels each token in a sentence with a fine-grained label from the full label set.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Expanded fine-grained context for Person and Location
    fine_label_context = {
        # Location subtypes
        Location_Facility: {'museum', 'tower', 'hall', 'center', 'castle', 'gallery', 'stadium', 'hospital', 'clinic', 'library', 'university', 'institute', 'station'},
        Location_OtherLOC: {'monument', 'bridge', 'site', 'landmark', 'road', 'highway', 'route'},
        Location_HumanSettlement: {'city', 'town', 'village', 'capital', 'metropolis', 'region', 'province', 'county', 'district', 'neighborhood', 'woodstock', 'york', 'paris'},
        Location_Station: {'station', 'terminal', 'depot', 'stop', 'hub', 'port', 'harbor', 'airport'},

        # Person subtypes
        Person_Scientist: {'physicist', 'biologist', 'chemist', 'researcher', 'professor', 'inventor', 'doctor'},
        Person_Artist: {'painter', 'sculptor', 'composer', 'poet', 'writer', 'illustrator', 'actor', 'singer'},
        Person_Athlete: {'player', 'athlete', 'runner', 'gymnast', 'boxer', 'swimmer', 'footballer'},
        Person_Politician: {'senator', 'president', 'minister', 'governor', 'emperor', 'king', 'queen', 'prime', 'leader'},
        Person_Cleric: {'bishop', 'priest', 'imam', 'rabbi', 'pastor', 'monk', 'nuncio'},
        Person_SportsManager: {'coach', 'manager', 'trainer', 'captain', 'director'},
        Person_OtherPER: {'author', 'historian', 'philosopher', 'child', 'founder', 'noble', 'ambassador', 'diplomat'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_CreativeWorks_Person(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on the context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for CreativeWorks and Person
    fine_label_context = {
        # CreativeWorks subtypes
        CreativeWorks_VisualWork: {'film', 'movie', 'art', 'painting', 'show', 'animation', 'series'},
        CreativeWorks_MusicalWork: {'album', 'song', 'symphony', 'track', 'composition'},
        CreativeWorks_WrittenWork: {'book', 'novel', 'poem', 'story', 'play'},
        CreativeWorks_ArtWork: {'sculpture', 'painting', 'masterpiece', 'portrait'},
        CreativeWorks_Software: {'software', 'program', 'application', 'tool'},
        
        # Person subtypes
        Person_Scientist: {'einstein', 'curie', 'tesla', 'darwin'},
        Person_Artist: {'painter', 'composer', 'sculptor', 'poet', 'writer'},
        Person_Athlete: {'player', 'athlete', 'runner', 'swimmer'},
        Person_Politician: {'king', 'queen', 'senator', 'president', 'minister'},
        Person_Cleric: {'priest', 'imam', 'bishop', 'monk'},
        Person_SportsManager: {'coach', 'trainer', 'captain'},
        Person_OtherPER: {'author', 'historian', 'philosopher', 'founder'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Person_Medical(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Person and Medical
    fine_label_context = {
        # Person subtypes
        Person_Scientist: {'murray', 'curie', 'einstein', 'darwin', 'researcher', 'biologist'},
        Person_Artist: {'composer', 'painter', 'sculptor', 'poet', 'actor', 'maharishi', 'yogi'},
        Person_Athlete: {'player', 'athlete', 'runner', 'gymnast', 'swimmer'},
        Person_Politician: {'senator', 'president', 'minister', 'leader', 'trudeau'},
        Person_Cleric: {'priest', 'imam', 'bishop', 'monk'},
        Person_SportsManager: {'coach', 'trainer', 'manager'},
        Person_OtherPER: {'author', 'critic', 'historian', 'philosopher', 'founder', 'joseph', 'shales'},
        
        # Medical subtypes
        MEDICAL_MEDICATION_VACCINE: {'drug', 'vaccine', 'medication', 'antibiotic'},
        Medical_MedicalProcedure: {'surgery', 'transplantation', 'therapy', 'meditation', 'procedure'},
        Medical_AnatomicalStructure: {'heart', 'brain', 'lung', 'kidney', 'muscle'},
        Medical_Symptom: {'pain', 'fatigue', 'fever', 'aids', 'cough', 'dizziness'},
        MEDICAL_DISEASE: {'cancer', 'diabetes', 'influenza', 'infection', 'disease'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Person_Group(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Person and Group
    fine_label_context = {
        # Person subtypes
        Person_Scientist: {'curie', 'einstein', 'darwin', 'murray'},
        Person_Artist: {'composer', 'painter', 'sculptor', 'poet', 'writer', 'drummer', 'singer', 'actor', 'jihyo', 'sharpe'},
        Person_Athlete: {'player', 'athlete', 'runner', 'gymnast'},
        Person_Politician: {'senator', 'president', 'minister', 'leader'},
        Person_Cleric: {'priest', 'imam', 'bishop', 'monk'},
        Person_SportsManager: {'coach', 'trainer', 'manager'},
        Person_OtherPER: {'author', 'historian', 'philosopher', 'founder', 'chairman', 'executive', 'charles', 'koch', 'tom', 'dennis', 'deyoung'},

        # Group subtypes
        Group_PublicCorp: {'corporation', 'inc', 'ltd', 'plc'},
        Group_PrivateCorp: {'koch', 'industries'},
        Group_AeroSpaceManufacturer: {'boeing', 'airbus', 'lockheed'},
        Group_SportsGRP: {'team', 'club', 'association'},
        Group_CarManufacturer: {'toyota', 'ford', 'mercedes'},
        Group_ORG: {'organization', 'agency', 'foundation'},
        Group_MusicalGroup: {'band', 'orchestra', 'choir', 'twice', 'steamroller'},
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Person_Product(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Person and Product
    fine_label_context = {
        # Person subtypes
        Person_Scientist: {'einstein', 'curie', 'murray', 'maunsell', 'howe', 'inventor'},
        Person_Artist: {'composer', 'painter', 'sculptor', 'poet', 'actor'},
        Person_Athlete: {'runner', 'swimmer', 'gymnast', 'wimille', 'driver'},
        Person_Politician: {'senator', 'president', 'minister'},
        Person_Cleric: {'priest', 'imam', 'bishop'},
        Person_SportsManager: {'coach', 'trainer', 'manager'},
        Person_OtherPER: {'author', 'critic', 'historian', 'philosopher', 'founder'},
        
        # Product subtypes
        Product_Clothing: {'shirt', 'dress', 'coat', 'jacket'},
        Product_Vehicle: {'car', 'truck', 'bike', 'alfa', 'romeo', 'k'},
        Product_Food: {'bread', 'fruit', 'cheese'},
        Product_Drink: {'soda', 'coffee', 'juice'},
        Product_OtherPROD: {'gadget', 'machine', 'sewing', 'device', 'tool'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_CreativeWorks_Group(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for CreativeWorks and Group
    fine_label_context = {
        # CreativeWorks subtypes
        CreativeWorks_VisualWork: {'film', 'movie', 'animation', 'series'},
        CreativeWorks_MusicalWork: {'album', 'song', 'track', 'composition', 'video', 'primera', 'fila', 'hecho', 'realidad'},
        CreativeWorks_WrittenWork: {'book', 'novel', 'poem', 'story', 'play'},
        CreativeWorks_ArtWork: {'painting', 'sculpture', 'portrait'},
        CreativeWorks_Software: {'software', 'application', 'program'},

        # Group subtypes
        Group_MusicalGroup: {'band', 'choir', 'orchestra', 'ensemble', 'ha*ash', 'orbital', 'stooges', 'modern', 'lovers', 'dolls'},
        Group_ORG: {'organization', 'foundation', 'agency'},
        Group_PublicCorp: {'corporation', 'inc', 'plc'},
        Group_PrivateCorp: {'ltd', 'gmbh'},
        Group_AeroSpaceManufacturer: {'boeing', 'airbus'},
        Group_SportsGRP: {'team', 'club'},
        Group_CarManufacturer: {'toyota', 'ford'},
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Location_Group(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Location and Group
    fine_label_context = {
        # Location subtypes
        Location_Facility: {'center', 'facility', 'complex', 'station', 'plant', 'headquarters'},
        Location_OtherLOC: {'monument', 'road', 'bridge', 'landmark'},
        Location_HumanSettlement: {'city', 'town', 'village', 'capital', 'metropolis', 'grangemouth', 'montana'},
        Location_Station: {'station', 'terminal', 'depot', 'airport'},

        # Group subtypes
        Group_ORG: {'organization', 'diocese', 'office', 'department', 'agency'},
        Group_PublicCorp: {'corporation', 'inc', 'plc', 'ineos', 'bp'},
        Group_PrivateCorp: {'ltd', 'gmbh'},
        Group_MusicalGroup: {'band', 'orchestra', 'ensemble'},
        Group_SportsGRP: {'team', 'club'},
        Group_AeroSpaceManufacturer: {'boeing', 'airbus'},
        Group_CarManufacturer: {'toyota', 'ford'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Medical_Person(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Medical and Person
    fine_label_context = {
        # Medical subtypes
        MEDICAL_MEDICATION_VACCINE: {'drug', 'vaccine', 'remedy', 'medication'},
        Medical_MedicalProcedure: {'surgery', 'therapy', 'procedure', 'treatment'},
        Medical_AnatomicalStructure: {'heart', 'brain', 'lung'},
        Medical_Symptom: {'migraine', 'pain', 'fever', 'dizziness'},
        MEDICAL_DISEASE: {'cancer', 'diabetes', 'meningitis', 'infection'},

        # Person subtypes
        Person_Scientist: {'curie', 'einstein', 'murray'},
        Person_Artist: {'painter', 'composer', 'poet'},
        Person_Athlete: {'player', 'athlete', 'runner', 'goalkeeper', 'grobbelaar'},
        Person_Politician: {'senator', 'president', 'minister'},
        Person_Cleric: {'priest', 'imam', 'bishop'},
        Person_SportsManager: {'coach', 'trainer', 'manager', 'skip'},
        Person_OtherPER: {'founder', 'historian', 'philosopher', 'catherine', 'jones', 'colleen'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Product_Group(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Product and Group
    fine_label_context = {
        # Product subtypes
        Product_Clothing: {'shirt', 'jacket', 'hat'},
        Product_Vehicle: {'car', 'bike', 'motorcycle'},
        Product_Food: {'bread', 'cheese', 'fruit'},
        Product_Drink: {'soda', 'juice', 'wine'},
        Product_OtherPROD: {'microcassette', 'playstation', 'console', 'audio', 'technology'},

        # Group subtypes
        Group_MusicalGroup: {'band', 'orchestra', 'ensemble', 'tokyo', 'ska', 'paradise'},
        Group_ORG: {'agency', 'foundation', 'association'},
        Group_PublicCorp: {'inc', 'plc'},
        Group_PrivateCorp: {'ltd', 'gmbh', 'taito', 'panasonic'},
        Group_SportsGRP: {'team', 'club'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Location_Medical(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Location and Medical
    fine_label_context = {
        # Location subtypes
        Location_Facility: {'hospital', 'clinic', 'prison', 'center', 'laboratory', 'kresty'},
        Location_OtherLOC: {'monument', 'street', 'road', 'bridge'},
        Location_HumanSettlement: {'city', 'town', 'village', 'capital', 'san', 'carlos', 'panama'},
        Location_Station: {'station', 'terminal', 'airport'},

        # Medical subtypes
        MEDICAL_MEDICATION_VACCINE: {'vaccine', 'drug', 'medication'},
        Medical_MedicalProcedure: {'surgery', 'appendectomy', 'therapy', 'procedure'},
        Medical_AnatomicalStructure: {'heart', 'lung', 'brain', 'tumor'},
        Medical_Symptom: {'pain', 'fatigue', 'cough'},
        MEDICAL_DISEASE: {'cancer', 'infection', 'diabetes'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Medical_Group(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Medical and Group
    fine_label_context = {
        # Medical subtypes
        MEDICAL_MEDICATION_VACCINE: {'drug', 'vaccine', 'medication', 'analgesic', 'alirocumab'},
        Medical_MedicalProcedure: {'surgery', 'therapy', 'procedure'},
        Medical_AnatomicalStructure: {'heart', 'brain', 'lung'},
        Medical_Symptom: {'pain', 'fatigue', 'cough'},
        MEDICAL_DISEASE: {'cancer', 'infection', 'deficiency'},

        # Group subtypes
        Group_PublicCorp: {'pfizer', 'sanofi'},
        Group_PrivateCorp: {'regeneron', 'gmbh'},
        Group_ORG: {'association', 'agency', 'pharmaceuticals'},
        Group_MusicalGroup: {'band', 'orchestra'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

def label_sentence_Product_Medical(tokens):
    """
    Labels each token in a sentence with a fine-grained label based on context.
    Returns a list of fine-grained labels for each token.
    
    Args:
    tokens: list of str - A list of words representing a sentence.
    
    Returns:
    list of str - A list of fine-grained labels for each token.
    """
    # Define fine-grained context for Product and Medical
    fine_label_context = {
        # Product subtypes
        Product_Clothing: {'shirt', 'jacket', 'uniform'},
        Product_Vehicle: {'car', 'truck', 'bike', 'prototype'},
        Product_Food: {'bread', 'cheese'},
        Product_Drink: {'wine', 'soda', 'ethanol'},
        Product_OtherPROD: {'device', 'tool', 'beverages', 'bodywork', 'chassis'},

        # Medical subtypes
        MEDICAL_MEDICATION_VACCINE: {'medication', 'drug', 'vaccine', 'medications'},
        MEDICAL_MEDICATION_VACCINE: {'medication', 'drug', 'vaccine', 'medications'},
        Medical_MedicalProcedure: {'surgery', 'operation', 'procedure'},
        Medical_AnatomicalStructure: {'eye', 'heart', 'brain'},
        Medical_Symptom: {'pain', 'fatigue'},
        MEDICAL_DISEASE: {'cancer', 'infection'}
    }

    labels = []

    for token in tokens:
        token_lower = token.lower()
        fine_label = ABSTAIN  # Default label

        for label, keywords in fine_label_context.items():
            if token_lower in keywords:
                fine_label = label
                break

        labels.append(fine_label)

    return labels

