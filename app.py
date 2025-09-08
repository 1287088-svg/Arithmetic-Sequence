import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence based on the given parameters.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def validate_inputs(first_term, common_difference, num_terms):
    """
    Validate user inputs for the arithmetic sequence generator.
    
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if number of terms is valid
    if num_terms <= 0:
        return False, "Number of terms must be a positive integer greater than 0."
    
    if num_terms > 1000:
        return False, "Number of terms cannot exceed 1000 for performance reasons."
    
    return True, ""

def main():
    """Main function to run the Streamlit application."""
    
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Application header
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="The number of terms to generate (1-1000)"
        )
    
    # Validate inputs
    is_valid, error_message = validate_inputs(first_term, common_difference, num_terms)
    
    if not is_valid:
        st.error(error_message)
        return
    
    # Generate sequence button
    if st.button("Generate Sequence", type="primary"):
        # Generate the arithmetic sequence
        sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
        
        # Display results
        st.header("Generated Arithmetic Sequence")
        
        # Show sequence formula
        st.markdown("**Formula:** aₙ = a₁ + (n-1) × d")
        st.markdown(f"**Your formula:** aₙ = {first_term} + (n-1) × {common_difference}")
        
        # Display sequence information
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("First Term", first_term)
        with col2:
            st.metric("Common Difference", common_difference)
        with col3:
            st.metric("Number of Terms", int(num_terms))
        
        # Display the sequence
        st.subheader("Sequence Terms")
        
        # Format sequence for display
        if len(sequence) <= 20:
            # For small sequences, display all terms in a nice format
            sequence_str = ", ".join([str(term) if term == int(term) else f"{term:.2f}" for term in sequence])
            st.write(f"**{sequence_str}**")
        else:
            # For large sequences, show first 10 and last 10 terms
            first_10 = sequence[:10]
            last_10 = sequence[-10:]
            
            first_str = ", ".join([str(term) if term == int(term) else f"{term:.2f}" for term in first_10])
            last_str = ", ".join([str(term) if term == int(term) else f"{term:.2f}" for term in last_10])
            
            st.write(f"**First 10 terms:** {first_str}")
            st.write("...")
            st.write(f"**Last 10 terms:** {last_str}")
        
        # Display additional information
        st.subheader("Sequence Information")
        
        info_col1, info_col2 = st.columns(2)
        
        with info_col1:
            st.write(f"**Sum of sequence:** {sum(sequence):.2f}")
            if len(sequence) > 1:
                st.write(f"**Range:** {min(sequence):.2f} to {max(sequence):.2f}")
        
        with info_col2:
            if len(sequence) > 0:
                avg = sum(sequence) / len(sequence)
                st.write(f"**Average:** {avg:.2f}")
                st.write(f"**Last term:** {sequence[-1]:.2f}")
        
        # Show sequence as a table for detailed view
        if st.checkbox("Show detailed table view"):
            import pandas as pd
            
            # Create DataFrame for table display
            df_data = []
            for i, term in enumerate(sequence, 1):
                df_data.append({
                    "Position (n)": i,
                    "Term Value (aₙ)": term,
                    "Calculation": f"{first_term} + ({i-1}) × {common_difference} = {term}"
                })
            
            df = pd.DataFrame(df_data)
            st.dataframe(df, use_container_width=True)
    
    # Information section
    st.markdown("---")
    st.markdown("### About Arithmetic Sequences")
    st.markdown("""
    An arithmetic sequence is a sequence of numbers where the difference between consecutive terms is constant.
    
    **Formula:** aₙ = a₁ + (n-1) × d
    
    Where:
    - aₙ is the nth term
    - a₁ is the first term
    - d is the common difference
    - n is the position of the term
    
    **Examples:**
    - Sequence: 2, 5, 8, 11, 14... (first term = 2, common difference = 3)
    - Sequence: 10, 7, 4, 1, -2... (first term = 10, common difference = -3)
    """)

if __name__ == "__main__":
    main()
