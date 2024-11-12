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

def label_otherper(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Person-OtherPER' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Person-OtherPER' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    titles_and_relationships = ['emperor', 'king', 'queen', 'lord', 'marquess', 'duke', 'prince', 'princess', 'brother', 'sister', 'father', 'mother', 'son', 'daughter']
    suffixes = ['jr', 'sr', 'ii', 'iii', 'iv']
    conjunctions = ['and']
    
    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == 'Person':
            lower_token = token.lower()
            
            # Check for linguistic patterns indicative of 'OtherPER'
            if (lower_token in titles_and_relationships) or \
               (i < len(tokens) - 1 and tokens[i + 1].lower() in suffixes) or \
               (i > 0 and tokens[i - 1].lower() in conjunctions):
                fine_labels.append(Person_OtherPER)
            elif i > 0 and tokens[i - 1].lower() in titles_and_relationships:
                fine_labels.append(Person_OtherPER)
            elif i > 1 and tokens[i - 2].lower() in conjunctions and coarse_labels[i - 1] == 'Person':
                fine_labels.append(Person_OtherPER)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels


def label_artist(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label Person_Artist based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with Person_Artist where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    artist_keywords = ['singer', 'musician', 'composer', 'painter', 'actor', 'actress', 'guitarist', 'poet', 'dancer', 'lyricist', 'artist', 'novelist', 'presenter']
    artistic_roles = ['lead', 'backing', 'performer', 'star', 'conductor', 'director', 'producer']
    
    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Person':
            # Check for direct keywords indicating artists
            if lower_token in artist_keywords:
                fine_labels.append(Person_Artist)
            # Check for surrounding words that may indicate artistic roles
            elif i > 0 and tokens[i - 1].lower() in artist_keywords:
                fine_labels.append(Person_Artist)
            elif i < len(tokens) - 1 and tokens[i + 1].lower() in artist_keywords:
                fine_labels.append(Person_Artist)
            elif i > 0 and tokens[i - 1].lower() in artistic_roles:
                fine_labels.append(Person_Artist)
            elif i < len(tokens) - 1 and tokens[i + 1].lower() in artistic_roles:
                fine_labels.append(Person_Artist)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_sportsgrp(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Group-SportsGRP' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Group-SportsGRP' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    sports_indicators = ['team', 'club', 'athletic', 'national', 'league', 'hall', 'fame']
    common_sports_terms = ['basketball', 'soccer', 'ski', 'football', 'hockey', 'rugby', 'baseball']

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Group':
            # Check if token matches common sports group indicators or sports terms
            if lower_token in sports_indicators or lower_token in common_sports_terms:
                fine_labels.append(Group_SportsGRP)
            # Check surrounding context for additional sports group indications
            elif (i > 0 and tokens[i - 1].lower() in sports_indicators) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in sports_indicators):
                fine_labels.append(Group_SportsGRP)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels


def label_athlete(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label Person_Athlete based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with Person_Athlete where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    athlete_keywords = ['player', 'champion', 'runner', 'driver', 'goalkeeper', 'pitcher', 'batsman', 'cricketer', 'tennis', 'footballer']
    sports_verbs = ['scored', 'rushed', 'played', 'won', 'qualified', 'competed', 'defended', 'saved']

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Person':
            # Check for direct keywords indicating athletes
            if lower_token in athlete_keywords:
                fine_labels.append(Person_Athlete)
            # Check surrounding context for athletic activity
            elif (i > 0 and tokens[i - 1].lower() in athlete_keywords) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in athlete_keywords):
                fine_labels.append(Person_Athlete)
            elif i > 0 and tokens[i - 1].lower() in sports_verbs:
                fine_labels.append(Person_Athlete)
            elif i < len(tokens) - 1 and tokens[i + 1].lower() in sports_verbs:
                fine_labels.append(Person_Athlete)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_org(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Group-ORG' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Group-ORG' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    org_indicators = ['bureau', 'federation', 'party', 'congress', 'parliament', 'metro', 'university', 'media', 'corporation', 'institute', 'commission', 'agency', 'association']
    org_suffixes = ['inc', 'ltd', 'corp', 'llc', 'gmbh']

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Group':
            # Check for direct organization indicators
            if lower_token in org_indicators or lower_token.endswith(tuple(org_suffixes)):
                fine_labels.append(Group_ORG)
            # Check surrounding tokens for context indicating organizations
            elif (i > 0 and tokens[i - 1].lower() in org_indicators) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in org_indicators):
                fine_labels.append(Group_ORG)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_medication(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Medical-Medication/Vaccine' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Medical-Medication/Vaccine' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    medication_indicators = ['vaccine', 'medication', 'drug', 'therapy', 'treatment']
    common_medications = ['aspirin', 'prednisone', 'letrozole', 'misoprostol', 'artemether', 'saquinavir', 'ritonavir', 'indinavir', 'thiamine', 'calcium', 'enzalutamide', 'abiraterone']
    suffixes = ['azole', 'vir', 'cillin', 'mab', 'xan', 'ine', 'ium']

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Medical':
            # Check for direct mentions of known medications
            if lower_token in common_medications or any(lower_token.endswith(suffix) for suffix in suffixes):
                fine_labels.append(MEDICAL_MEDICATION_VACCINE)
            # Check for surrounding context that may indicate medication
            elif (i > 0 and tokens[i - 1].lower() in medication_indicators) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in medication_indicators):
                fine_labels.append(MEDICAL_MEDICATION_VACCINE)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_disease(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Medical-Disease' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Medical-Disease' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    disease_keywords = ['disease', 'disorder', 'syndrome', 'illness', 'infection', 'condition', 'cancer', 'arthritis', 'psychosis', 'obsessive–compulsive']
    disease_suffixes = ['itis', 'osis', 'pathy', 'emia', 'oma', 'algia']

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Medical':
            # Check for direct mentions of known disease-related words
            if lower_token in disease_keywords or any(lower_token.endswith(suffix) for suffix in disease_suffixes):
                fine_labels.append(MEDICAL_DISEASE)
            # Check for context indicating a medical condition (e.g., adjacent words)
            elif (i > 0 and tokens[i - 1].lower() in disease_keywords) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in disease_keywords):
                fine_labels.append(MEDICAL_DISEASE)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_human_settlement(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Location-HumanSettlement' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Location-HumanSettlement' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    settlement_indicators = ['city', 'capital', 'village', 'town', 'borough']
    multi_word_locations = {'united states', 'new zealand', 'south africa', 'united kingdom', 'hong kong', 'sri lanka'}

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Location':
            # Check if token is part of known multi-word location names
            if i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in multi_word_locations:
                fine_labels.append(Location_HumanSettlement)
            # Check for common indicators of human settlements
            elif lower_token in settlement_indicators:
                fine_labels.append(Location_HumanSettlement)
            # Check if the token is likely a country or major city (could be extended with a more comprehensive list)
            elif lower_token in {'boston', 'russia', 'japan', 'opole', 'karoonda'}:
                fine_labels.append(Location_HumanSettlement)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_public_corp(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Group-PublicCorp' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Group-PublicCorp' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    public_corp_indicators = ['corporation', 'company', 'inc', 'group', 'media', 'bank', 'railway', 'refinery']
    known_public_corps = {
        'disney', 'ecopetrol', 'cumulus', 'oricon', 'vf corporation',
        'commonwealth banking corporation', 'jr east', 'john deere', 'norfolk southern'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Group':
            # Check if token matches known public corporation names or indicators
            if lower_token in known_public_corps or lower_token in public_corp_indicators:
                fine_labels.append(Group_PublicCorp)
            # Check if token is followed or preceded by common public corporation terms
            elif (i > 0 and tokens[i - 1].lower() in public_corp_indicators) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in public_corp_indicators):
                fine_labels.append(Group_PublicCorp)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_visual_work(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'CreativeWorks-VisualWork' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'CreativeWorks-VisualWork' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    visual_work_indicators = ['movie', 'film', 'show', 'series', 'cinematic', 'picture', 'episode', 'feature']
    known_visual_works = {
        'citizen kane', 'psycho-pass', 'battle of memories', 'makante achan',
        'the lion of st.', 'prancer'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'CreativeWorks':
            # Check if token matches known visual work names or indicators
            if lower_token in visual_work_indicators or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in known_visual_works):
                fine_labels.append(CreativeWorks_VisualWork)
            # Check if the token is part of multi-word visual works
            elif any(lower_token.startswith(work.split()[0]) for work in known_visual_works):
                fine_labels.append(CreativeWorks_VisualWork)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_vehicle(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Product-Vehicle' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Product-Vehicle' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    vehicle_keywords = ['car', 'truck', 'jeepney', 'minibus', 'sedan', 'schooner', 'chassis', 'cutter', 'ship', 'vehicle', 'van', 'pocketbike']
    known_vehicles = {
        'holden monaro', 'cargo ship', 'amphibious cargo ship'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Product':
            # Check if token matches known vehicle names or types
            if lower_token in vehicle_keywords or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in known_vehicles):
                fine_labels.append(Product_Vehicle)
            # Check if the token is part of multi-word vehicle names
            elif any(lower_token.startswith(vehicle.split()[0]) for vehicle in known_vehicles):
                fine_labels.append(Product_Vehicle)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_facility(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Location-Facility' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Location-Facility' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    facility_keywords = ['arena', 'park', 'college', 'theatre', 'temple', 'palace', 'cemetery', 'prison']
    multi_word_facilities = {
        'crystal palace', 'reed arena', 'inner temple', 'vale park'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Location':
            # Check if token matches known facility names or indicators
            if lower_token in facility_keywords or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in multi_word_facilities):
                fine_labels.append(Location_Facility)
            # Check if the token is part of multi-word facility names
            elif any(lower_token.startswith(facility.split()[0]) for facility in multi_word_facilities):
                fine_labels.append(Location_Facility)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_other_prod(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Product-OtherPROD' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Product-OtherPROD' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    product_keywords = ['chair', 'gate', 'plane', 'wheelchair', 'carrier', 'layout', 'telescope', 'rudder', 'armored', 'prototypes']
    multi_word_products = {
        'windsor chair', 'hubble space telescope', 'pilatus pc-12', 'armored personnel carrier'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Product':
            # Check if token matches known product names or general product indicators
            if lower_token in product_keywords or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in multi_word_products):
                fine_labels.append(Product_OtherPROD)
            # Check if the token is part of multi-word product names
            elif any(lower_token.startswith(product.split()[0]) for product in multi_word_products):
                fine_labels.append(Product_OtherPROD)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_politician(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Person-Politician' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Person-Politician' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    political_titles = ['senator', 'governor', 'mayor', 'president', 'minister', 'secretary', 'chancellor', 'prime minister']
    known_politicians = {
        'augustus', 'dick durbin', 'victor hugo', 'john knox', 'hernán siles zuazo', 'karl von müller', 'sharon sayles belton'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'Person':
            # Check if token matches known politician names or follows a political title
            if lower_token in known_politicians or \
               (i > 0 and tokens[i - 1].lower() in political_titles):
                fine_labels.append(Person_Politician)
            # Check if multi-word names form a politician's name
            elif any(lower_token.startswith(name.split()[0]) for name in known_politicians):
                fine_labels.append(Person_Politician)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label=='O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_written_work(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'CreativeWorks-WrittenWork' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'CreativeWorks-WrittenWork' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    written_work_keywords = ['book', 'novel', 'story', 'magazine', 'press', 'newspaper', 'review', 'miniseries', 'comic']
    known_written_works = {
        'guinness book of records', 'new york times', 'times', 'oberlin review', 'cleveland press', 'phantom of the opera', 'national register of historic places'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'CreativeWorks':
            # Check if token matches known written work titles or keywords
            if lower_token in written_work_keywords or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in known_written_works):
                fine_labels.append(CreativeWorks_WrittenWork)
            # Check if the token is part of multi-word written work names
            elif any(lower_token.startswith(work.split()[0]) for work in known_written_works):
                fine_labels.append(CreativeWorks_WrittenWork)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else :
            fine_labels.append(ABSTAIN)
    
    return fine_labels

def label_software(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'CreativeWorks-Software' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'CreativeWorks-Software' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    software_keywords = ['game', 'application', 'software', 'platform', 'bios', 'network']
    known_software_names = {
        'minecraft', 'facebook', 'bios', 'r-type delta', 'bbc radio 1', 'private internet access', 'turok', 'degas'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()
        
        if coarse_label == 'CreativeWorks':
            # Check if token matches known software names or keywords related to software
            if lower_token in known_software_names or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in known_software_names):
                fine_labels.append(CreativeWorks_Software)
            # Check if the token is part of multi-word software names
            elif any(lower_token.startswith(software.split()[0]) for software in known_software_names):
                fine_labels.append(CreativeWorks_Software)
            elif lower_token in software_keywords:
                fine_labels.append(CreativeWorks_Software)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)  
    
    return fine_labels

def label_otherloc(tokens, coarse_labels):
    """
    Labelling function to assign the fine-grained label 'Location-OtherLOC' based on given tokens and coarse labels.
    
    Parameters:
    tokens (list): List of words (tokens) in a sentence.
    coarse_labels (list): List of coarse labels corresponding to each token.

    Returns:
    list: List of labels with 'Location-OtherLOC' where appropriate, or 'O' otherwise.
    """
    
    fine_labels = []
    location_keywords = ['museum', 'academy', 'center', 'arena', 'garden', 'park', 'grounds', 'cemetery', 'hall', 'exhibit']
    known_location_phrases = {
        'crystal palace', 'royal canadian academy of arts', 'daskalakis athletic center', 'little sparta'
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        lower_token = token.lower()

        if coarse_label == 'Location':
            # Check if token matches known location phrases or keywords related to specific types of locations
            if lower_token in location_keywords or \
               (i < len(tokens) - 1 and f"{lower_token} {tokens[i + 1].lower()}" in known_location_phrases):
                fine_labels.append(Location_OtherLOC)
            elif any(lower_token.startswith(phrase.split()[0]) for phrase in known_location_phrases):
                fine_labels.append(Location_OtherLOC)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == 'O':
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)
    
    return fine_labels



def label_food(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Product-Food'.
    """
    # List of known food-related keywords based on provided examples
    food_keywords = {
        "seafood", "grains", "flour", "sugar", "rice", "cake", "broth", "spaghetti", 
        "linguine", "paccheri", "chutneys", "achars", "oil", "lemang", "durian", 
        "offal", "meat", "goat", "lamb", "mutton", "beef"
    }

    # Placeholder for fine-grained labels
    fine_labels = []

    for token, coarse_label in zip(tokens, coarse_labels):
        if coarse_label == "Product" and token.lower() in food_keywords:
            fine_labels.append(Product_Food)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_musical_work(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'CreativeWorks-MusicalWork'.
    """
    # List of known musical work-related keywords based on provided examples
    musical_keywords = {
        "songs", "album", "single", "sonatas", "march", "rock", "blues", "reggae",
        "symphony", "concerto", "aria", "opera", "record", "score"
    }

    # Placeholder for fine-grained labels
    fine_labels = []

    for token, coarse_label in zip(tokens, coarse_labels):
        if coarse_label == "CreativeWorks" and token.lower() in musical_keywords:
            fine_labels.append(CreativeWorks_MusicalWork)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels


def label_scientist(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Person-Scientist'.
    """
    # List of known scientist-related keywords based on provided examples
    scientist_indicators = {
        "engineer", "scientist", "theorist", "historian", "astronaut", "advisor", 
        "creator", "healer", "inventor", "chemist", "physicist", "biologist"
    }

    # Placeholder for fine-grained labels
    fine_labels = []

    for token, coarse_label in zip(tokens, coarse_labels):
        if coarse_label == "Person" and token.lower() in scientist_indicators:
            fine_labels.append(Person_Scientist)
        elif coarse_label == "O":
            fine_labels.append(O)
        else:
            fine_labels.append(ABSTAIN)  # Default to 'O' if not a match

    return fine_labels


def label_sports_manager(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Person-SportsManager'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        # Check if the token is labeled as a 'Person'
        if coarse_label == "Person":
            # Check for preceding or following words that indicate sports management context
            if (i > 0 and tokens[i - 1].lower() in {"coach", "manager", "assistant", "director", "head"}) or \
               (i < len(tokens) - 1 and tokens[i + 1].lower() in {"coach", "manager", "assistant", "director", "head", "trainer", "captain"}):
                fine_labels.append(Person_SportsManager)
            # Check if the token itself is part of a role phrase
            elif token.lower() in {"coach", "manager", "trainer", "director"}:
                fine_labels.append(Person_SportsManager)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_musical_group(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Group-MusicalGRP'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of indicators that suggest a musical group context
    group_indicators = {"band", "duo", "ensemble", "choir", "orchestra", "group", "collective"}

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Group":
            # Check context words before and after for group indicators
            if (i > 0 and tokens[i - 1].lower() in group_indicators) or \
               (i < len(tokens) - 1 and tokens[i + 1].lower() in group_indicators):
                fine_labels.append(Group_MusicalGroup)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else: 
            fine_labels.append(ABSTAIN)    

    return fine_labels

def label_anatomical_structure(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Medical-AnatomicalStructure'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of indicators or anatomical terms that suggest context for anatomical structures
    anatomical_indicators = {
        "artery", "vein", "nerve", "muscle", "tendon", "bone", "joint", "skin", "organ", "tissue",
        "inflorescence", "stalk", "leaf", "leaves", "bill", "carpel", "stamen", "petiole", "foot", "head", "leg"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Medical":
            # Check for exact matches in the known anatomical indicators set
            if token.lower() in anatomical_indicators:
                fine_labels.append(Medical_AnatomicalStructure)
            # Check for surrounding words that might indicate anatomical context
            elif (i > 0 and tokens[i - 1].lower() in {"the", "a", "an", "its"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"structure", "surface", "side", "region"}):
                fine_labels.append(Medical_AnatomicalStructure)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels


def label_clothing(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Product-Clothing'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of indicators or terms related to clothing items
    clothing_indicators = {
        "shirt", "hat", "dress", "cap", "mask", "coat", "helmet", "scarf", "moccasin", "suit",
        "jacket", "glove", "boot", "robe", "tunic", "cloak", "uniform", "sweater", "umbrella",
        "sandal", "shoe", "sock", "sheath", "collar"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Product":
            # Check if the token matches known clothing terms
            if token.lower() in clothing_indicators:
                fine_labels.append(Product_Clothing)
            # Context-based check for preceding or following descriptors
            elif (i > 0 and tokens[i - 1].lower() in {"traditional", "ritual", "ceremonial", "protective", "signature"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"wear", "garment", "attire"}):
                fine_labels.append(Product_Clothing)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_cleric(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Person-Cleric'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of titles and indicators related to clerics
    cleric_indicators = {
        "pope", "bishop", "father", "saint", "st.", "pastor", "reverend", "imam", 
        "rabbi", "monk", "priest", "metropolitan", "abbot", "lama", "rinpoche"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Person":
            # Check if the token matches known cleric titles or has contextual indicators
            if token.lower() in cleric_indicators:
                fine_labels.append(Person_Cleric)
            # Check for surrounding context indicating a cleric, e.g., titles like "Saint"
            elif (i > 0 and tokens[i - 1].lower() in {"father", "saint", "reverend", "metropolitan"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"theologian", "preacher"}):
                fine_labels.append(Person_Cleric)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels


def label_medical_procedure(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Medical-MedicalProcedure'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known medical procedures and contextual indicators
    medical_procedure_indicators = {
        "surgery", "amputation", "tracheotomy", "injection", "abortion", "sonogram",
        "therapy", "treatment", "healing", "procedure", "traction"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Medical":
            # Check if the token matches known medical procedure terms
            if token.lower() in medical_procedure_indicators:
                fine_labels.append(Medical_MedicalProcedure)
            # Context-based check for words indicating medical actions
            elif (i > 0 and tokens[i - 1].lower() in {"surgical", "cardiac", "physical", "open", "intraperitoneal"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"therapy", "treatment", "procedure", "operation"}):
                fine_labels.append(Medical_MedicalProcedure)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_station(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Location-Station'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known station-related terms and contextual indicators
    station_indicators = {
        "station", "depot", "terminal", "airport", "airbase", "port", "railway", "bus", "tube"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Location":
            # Check if the token matches known station terms
            if token.lower() in station_indicators:
                fine_labels.append(Location_Station)
            # Context-based checks for preceding or following relevant words
            elif (i > 0 and tokens[i - 1].lower() in {"train", "bus", "tube", "air"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"station", "depot", "port", "base", "airport"}):
                fine_labels.append(Location_Station)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_car_manufacturer(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Group-CarManufacturer'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known car manufacturers and contextual indicators
    car_manufacturer_indicators = {
        "ford", "chevrolet", "mazda", "renault", "audi", "hyundai", "dodge", "rolls-royce", "clénet", "werner"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Group":
            # Check if the token matches known car manufacturer names
            if token.lower() in car_manufacturer_indicators:
                fine_labels.append(Group_CarManufacturer)
            # Contextual check for surrounding words that indicate a car-related entity
            elif (i > 0 and tokens[i - 1].lower() in {"motor", "automobile", "car"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"motors", "automobiles", "company", "group"}):
                fine_labels.append(Group_CarManufacturer)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels
def label_drink(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Product-Drink'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known drink-related terms and contextual indicators
    drink_indicators = {
        "wine", "tequila", "prosecco", "ale", "juice", "syrup", "pepsi", "chicha", "coors", "coffee",
        "beer", "soda", "cocktail", "liqueur", "milk", "tea", "whiskey", "gin", "rum", "brandy"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Product":
            # Check if the token matches known drink terms
            if token.lower() in drink_indicators:
                fine_labels.append(Product_Drink)
            # Contextual check for surrounding words indicating drinks
            elif (i > 0 and tokens[i - 1].lower() in {"carbonated", "alcoholic", "soft", "cold", "hot"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"drink", "beverage"}):
                fine_labels.append(Product_Drink)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels


def label_aerospace_manufacturer(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Group-AerospaceManufacturer'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known aerospace manufacturers and contextual indicators
    aerospace_indicators = {
        "boeing", "lockheed", "airbus", "avro", "potez", "orbital", "atk", "short", "mbda",
        "avic", "aviolanda", "bombardier"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Group":
            # Check if the token matches known aerospace manufacturer names
            if token.lower() in aerospace_indicators:
                fine_labels.append(Group_AeroSpaceManufacturer)
            # Contextual check for surrounding words indicating aerospace manufacturing
            elif (i > 0 and tokens[i - 1].lower() in {"aerospace", "aircraft", "aviation"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"corporation", "industries", "inc.", "company"}):
                fine_labels.append(Group_AeroSpaceManufacturer)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_symptom(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Medical-Symptom'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known symptom-related terms and contextual indicators
    symptom_indicators = {
        "anxiety", "inflammation", "oedema", "paralysis", "fatigue", "burnout", "itchy", "whitening", 
        "pain", "dizziness", "nausea", "fever", "cough", "headache", "insomnia", "chills", "tremors", "seizure"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Medical":
            # Check if the token matches known symptom terms
            if token.lower() in symptom_indicators:
                fine_labels.append(Medical_Symptom)
            # Contextual check for surrounding words indicating symptoms
            elif (i > 0 and tokens[i - 1].lower() in {"chronic", "acute", "severe", "persistent", "temporary"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"pain", "syndrome", "reaction", "episode"}):
                fine_labels.append(Medical_Symptom)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_artwork(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'CreativeWorks-ArtWork'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known artwork-related terms and contextual indicators
    artwork_indicators = {
        "painting", "sculpture", "murals", "handscroll", "portrait", "installation", "artwork", 
        "work", "piece", "masterpiece", "fresco"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "CreativeWorks":
            # Check if the token matches known artwork terms
            if token.lower() in artwork_indicators:
                fine_labels.append(CreativeWorks_ArtWork)
            # Contextual check for surrounding words indicating art pieces
            elif (i > 0 and tokens[i - 1].lower() in {"famous", "known", "historical", "classic"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"painting", "sculpture", "piece", "masterpiece"}):
                fine_labels.append(CreativeWorks_ArtWork)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_private_corp(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically focusing on identifying 'Group-PrivateCorp'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # List of known private corporation indicators and contextual hints
    private_corp_indicators = {
        "gmbh", "llc", "ltd", "inc", "aps", "bv", "nfl", "hallmark", "trinity", "hedge", "fund"
    }

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        if coarse_label == "Group":
            # Check if the token matches known private corporation names or abbreviations
            if token.lower() in private_corp_indicators:
                fine_labels.append(Group_PrivateCorp)
            # Contextual check for surrounding words indicating private corporations
            elif (i > 0 and tokens[i - 1].lower() in {"company", "corporation", "firm", "enterprise"}) or \
                 (i < len(tokens) - 1 and tokens[i + 1].lower() in {"inc.", "limited", "corporation", "enterprise"}):
                fine_labels.append(Group_PrivateCorp)
            else:
                fine_labels.append(ABSTAIN)
        elif coarse_label == "O":
            fine_labels.append(O)  # Default to 'O' if not a match
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_location_person(tokens, coarse_labels):
    """
    This function takes a list of tokens (words in a sentence) and a corresponding list of coarse labels,
    and returns a list of fine-grained labels, specifically identifying 'Location' (e.g., HumanSettlement, Facility)
    and 'Person' (e.g., Artist, OtherPER).
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # Known indicators for specific types of locations and persons
    location_indicators = {
        "woodstock": Location_HumanSettlement,
        "new york": Location_HumanSettlement,
        "trim castle": Location_Facility,
        "kilkea castle": Location_Facility,
        "ming dynasty": Location_HumanSettlement
    }
    
    person_indicators = {
        "desmond child": Person_Artist,
        "walter": Person_OtherPER,
        "yongle emperor": Person_OtherPER
    }

    # Iterate through tokens and label accordingly
    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Location":
            if token_lower in location_indicators:
                fine_labels.append(location_indicators[token_lower])
            else:
                fine_labels.append(Location_OtherLOC)  # Default to generic location if no specific match

        elif coarse_label == "Person":
            if token_lower in person_indicators:
                fine_labels.append(person_indicators[token_lower])
            else:
                fine_labels.append(Person_OtherPER)  # Default to generic person if no specific match

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_creativeworks_person(tokens, coarse_labels):
    """
    This function takes a list of tokens and their corresponding coarse labels, 
    and returns a list of fine-grained labels for 'CreativeWorks' and 'Person'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # Known indicators for specific types of CreativeWorks and Persons
    creativeworks_indicators = {
        "album": CreativeWorks_MusicalWork,
        "painting": CreativeWorks_ArtWork,
        "star": CreativeWorks_MusicalWork,
        "abigail": CreativeWorks_MusicalWork,
        "bacchus": CreativeWorks_ArtWork,
        "ariadne": CreativeWorks_ArtWork
    }
    
    person_indicators = {
        "king": Person_Artist,
        "diamond": Person_Artist,
        "titian": Person_Artist,
        "oscar": Person_Artist,
        "hammerstein": Person_Artist,
        "jerome": Person_Artist,
        "kern": Person_Artist
    }

    # Iterate through tokens and label accordingly
    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "CreativeWorks":
            if token_lower in creativeworks_indicators:
                fine_labels.append(creativeworks_indicators[token_lower])
            else:
                fine_labels.append(ABSTAIN)  # Default if no specific match

        elif coarse_label == "Person":
            if token_lower in person_indicators:
                fine_labels.append(person_indicators[token_lower])
            else:
                fine_labels.append(ABSTAIN)  # Default if no specific match

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_person_group(tokens, coarse_labels):
    """
    This function labels tokens with fine-grained labels for 'Person' and 'Group'.
    """
    # Placeholder for fine-grained labels
    fine_labels = []

    # Known indicators for specific Person and Group labels
    person_indicators = {
        "charles": Person_OtherPER,
        "koch": Person_OtherPER,
        "jihyo": Person_Artist,
        "tom": Person_Artist,
        "sharpe": Person_Artist,
        "dennis": Person_Artist,
        "deyoung": Person_Artist
    }

    group_indicators = {
        "koch": Group_PrivateCorp,
        "industries": Group_PrivateCorp,
        "twice": Group_MusicalGroup,
        "mannheim": Group_MusicalGroup,
        "steamroller": Group_MusicalGroup
    }

    # Iterate through tokens and label accordingly
    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Person":
            if token_lower in person_indicators:
                fine_labels.append(person_indicators[token_lower])
            else:
                fine_labels.append(ABSTAIN)  # Default if no specific match

        elif coarse_label == "Group":
            if token_lower in group_indicators:
                fine_labels.append(group_indicators[token_lower])
            else:
                fine_labels.append(ABSTAIN)  # Default if no specific match

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_person_group(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on coarse labels for 'Person' and 'Group'.
    """
    fine_labels = []
    
    # Dictionaries with known person and group labels for more specific classification
    person_indicators = {
        "charles": Person_OtherPER,
        "koch": Person_OtherPER,
        "jihyo": Person_Artist,
        "tom": Person_Artist,
        "sharpe": Person_Artist,
        "dennis": Person_Artist,
        "deyoung": Person_Artist
    }

    group_indicators = {
        "koch": Group_PrivateCorp,
        "industries": Group_PrivateCorp,
        "twice": Group_MusicalGroup,
        "mannheim": Group_MusicalGroup,
        "steamroller": Group_MusicalGroup
    }

    for token, coarse_label in zip(tokens, coarse_labels):
        token_lower = token.lower()

        if coarse_label == "Person":
            fine_labels.append(person_indicators.get(token_lower, ABSTAIN))  # Default label if no match

        elif coarse_label == "Group":
            fine_labels.append(group_indicators.get(token_lower, ABSTAIN))  # Default label if no match

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_person_product(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on coarse labels for 'Person' and 'Product'.
    """
    fine_labels = []
    
    # Dictionaries with known person and product labels for more specific classification
    person_indicators = {
        "elias": Person_Scientist,
        "howe": Person_Scientist,
        "jean-pierre": Person_Athlete,
        "wimille": Person_Athlete,
        "r.e.l.": Person_Scientist,
        "maunsell": Person_Scientist
    }

    product_indicators = {
        "sewing": Product_OtherPROD,
        "machine": Product_OtherPROD,
        "alfa": Product_OtherPROD,
        "romeo": Product_OtherPROD,
        "158": Product_OtherPROD,
        "k": Product_Vehicle,
        "class": Product_Vehicle,
        "secr": Product_Vehicle
    }

    for token, coarse_label in zip(tokens, coarse_labels):
        token_lower = token.lower()

        if coarse_label == "Person":
            fine_labels.append(person_indicators.get(token_lower, ABSTAIN))  # Default to "OtherPER"

        elif coarse_label == "Product":
            fine_labels.append(product_indicators.get(token_lower, ABSTAIN))  # Default to "OtherPROD"

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_creativeworks_group(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on coarse labels for 'CreativeWorks' and 'Group'.
    """
    fine_labels = []
    
    # Dictionaries with known creative works and groups for specific classification
    group_indicators = {
        "modern": Group_MusicalGroup,
        "lovers": Group_MusicalGroup,
        "new": Group_MusicalGroup,
        "york": Group_MusicalGroup,
        "dolls": Group_MusicalGroup,
        "stooges": Group_MusicalGroup,
        "ha*ash": Group_MusicalGroup,
        "orbital": Group_MusicalGroup
    }

    creativeworks_indicators = {
        "self-titled": CreativeWorks_MusicalWork,
        "album": CreativeWorks_MusicalWork,
        "primera": CreativeWorks_MusicalWork,
        "fila": CreativeWorks_MusicalWork,
        "hecho": CreativeWorks_MusicalWork,
        "realidad": CreativeWorks_MusicalWork,
        "the": CreativeWorks_MusicalWork,
        "box": CreativeWorks_MusicalWork
    }

    for token, coarse_label in zip(tokens, coarse_labels):
        token_lower = token.lower()

        if coarse_label == "Group":
            fine_labels.append(group_indicators.get(token_lower, ABSTAIN))  # Default to "OtherGRP"

        elif coarse_label == "CreativeWorks":
            fine_labels.append(creativeworks_indicators.get(token_lower, ABSTAIN))  # Default to "Other"

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels


def label_location_group(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on coarse labels for 'Location' and 'Group'.
    """
    fine_labels = []

    # Dictionaries to map specific tokens to fine-grained labels
    location_indicators = {
        "city": Location_HumanSettlement,
        "great": Location_HumanSettlement,
        "falls": Location_HumanSettlement,
        "montana": Location_HumanSettlement,
        "grangemouth": Location_HumanSettlement,
        "united": Location_HumanSettlement,
        "kingdom": Location_HumanSettlement
    }

    group_indicators = {
        "see": Group_ORG,
        "ineos": Group_PrivateCorp,
        "office": Group_ORG,
        "national": Group_ORG,
        "statistics": Group_ORG
    }

    for token, coarse_label in zip(tokens, coarse_labels):
        token_lower = token.lower()

        if coarse_label == "Location":
            fine_labels.append(location_indicators.get(token_lower, ABSTAIN))  # Default to "Other"

        elif coarse_label == "Group":
            fine_labels.append(group_indicators.get(token_lower, ABSTAIN))  # Default to "OtherGRP"

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_medical_person_with_context(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on linguistic context and coarse labels for 'Medical' and 'Person'.
    """
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Medical":
            # Check surrounding words for typical patterns indicating diseases or conditions
            if (i > 0 and tokens[i - 1].lower() in ["with", "from", "suffers", "suffering", "diagnosed"]) or \
               (i + 1 < len(tokens) and tokens[i + 1].lower() in ["attack", "infection", "disease"]):
                fine_labels.append(MEDICAL_DISEASE)
            else:
                fine_labels.append(ABSTAIN)
        
        elif coarse_label == "Person":
            # Identify titles or honorifics as indicators of person names
            if token_lower in ["dr", "mr", "mrs", "ms", "professor", "doctor", "sir"]:
                fine_labels.append(Person_OtherPER)
            # Check if a person's name is followed by words indicating their role or relationship
            elif i + 1 < len(tokens) and tokens[i + 1].lower() in ["said", "added", "explained", "reported"]:
                fine_labels.append(Person_OtherPER)
            elif i > 0 and tokens[i - 1].lower() in ["by", "from", "to"]:
                fine_labels.append(Person_OtherPER)
            else:
                fine_labels.append(ABSTAIN)
        
        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'
        
        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_product_group_with_context(tokens, coarse_labels):
    """
    Assigns fine-grained labels to tokens based on linguistic context and coarse labels for 'Product' and 'Group'.
    """
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Product":
            # Check if a product is mentioned alongside typical association verbs or prepositions
            if (i > 0 and tokens[i - 1].lower() in ["by", "from", "made", "produced", "released", "introduced"]) or \
               (i + 1 < len(tokens) and tokens[i + 1].lower() in ["from", "by"]):
                fine_labels.append(Product_OtherPROD)
            else:
                fine_labels.append(ABSTAIN)

        elif coarse_label == "Group":
            # Assign fine label based on context indicating a company, organization, or group
            if token_lower in ["inc", "ltd", "corp", "corporation", "company"]:
                fine_labels.append(Group_PublicCorp)
            elif i > 0 and tokens[i - 1].lower() in ["ex", "former", "member"]:
                fine_labels.append(Group_MusicalGroup)
            else:
                fine_labels.append(ABSTAIN)
        
        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_location_medical_with_context(tokens, coarse_labels):
    """
    Assigns fine-grained labels based on linguistic context for 'Location' and 'Medical' coarse labels.
    """
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Location":
            # Check if the location is associated with a medical context (preceding or following terms)
            if (i > 0 and coarse_labels[i - 1] == "Medical") or (i + 1 < len(coarse_labels) and coarse_labels[i + 1] == "Medical"):
                fine_labels.append(Location_Facility if token_lower in ["hospital", "clinic", "prison"] else Location_HumanSettlement)
            else:
                fine_labels.append(ABSTAIN)  # Default for general locations
        
        elif coarse_label == "Medical":
            # Assign fine labels for medical contexts directly
            fine_labels.append(Medical_MedicalProcedure if "surgery" in token_lower or "ectomy" in token_lower else MEDICAL_DISEASE)
        
        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_medical_group_with_context(tokens, coarse_labels):
    """
    Assigns fine-grained labels based on linguistic context for 'Medical' and 'Group' coarse labels.
    """
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Group":
            # Check if the group is associated with a medical term (e.g., a pharmaceutical company or research organization)
            if (i > 0 and coarse_labels[i - 1] == "Medical") or (i + 1 < len(coarse_labels) and coarse_labels[i + 1] == "Medical"):
                fine_labels.append(Group_PublicCorp)
            else:
                fine_labels.append(Group_ORG)  # Default for general groups
        
        elif coarse_label == "Medical":
            # Assign fine labels for medical contexts
            fine_labels.append(MEDICAL_MEDICATION_VACCINE if "drug" in token_lower or "medication" in token_lower else MEDICAL_DISEASE)
        
        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels

def label_product_medical_with_context(tokens, coarse_labels):
    """
    Assigns fine-grained labels based on linguistic context for 'Product' and 'Medical' coarse labels.
    """
    fine_labels = []

    for i, (token, coarse_label) in enumerate(zip(tokens, coarse_labels)):
        token_lower = token.lower()

        if coarse_label == "Product":
            # Check if the product is related to medical context (e.g., food used in treatments)
            if (i > 0 and coarse_labels[i - 1] == "Medical") or (i + 1 < len(coarse_labels) and coarse_labels[i + 1] == "Medical"):
                if "medications" in token_lower or "glasses" in token_lower:
                    fine_labels.append(Medical_MedicalProcedure)
                else:
                    fine_labels.append(Product_OtherPROD)
            else:
                fine_labels.append(O)  # Default for general products

        elif coarse_label == "Medical":
            # Label medical terms related to products
            fine_labels.append(MEDICAL_MEDICATION_VACCINE if "ethanol" in token_lower or "medications" in token_lower else Medical_MedicalProcedure)

        elif coarse_label == "O":
            fine_labels.append(O)  # Non-matching tokens are labeled as 'O'

        else:
            fine_labels.append(ABSTAIN)

    return fine_labels
