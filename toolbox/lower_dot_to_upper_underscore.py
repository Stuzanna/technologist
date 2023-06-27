def gw_converter(input):
    """
    Function for helping prep Conduktor Gateway -e variables.
    
    Convert boilerplate of "text.like.this" into "KAFKA_TEXT_LIKE_THIS"
    """
    upper = input.upper()
    underscored = upper.replace(".","_")
    result = underscored

    print(f"KAFKA_{result}")
    return result

gw_converter("sasl.jaas.config")