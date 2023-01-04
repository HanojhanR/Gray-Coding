def generate_pam_symbol_mapping(bitstream, pam_level, k, Tb, Ts, gray_code=True):
  # Validate the input parameters
  if not isinstance(bitstream, str) or not all(c in '01' for c in bitstream):
    raise ValueError('The bitstream must be a string of 0s and 1s.')
  if not isinstance(pam_level, int) or pam_level <= 0:
    raise ValueError('The PAM level must be a positive integer.')
  if not isinstance(k, int) or k <= 0:
    raise ValueError('The k parameter must be a positive integer.')
  if not isinstance(Tb, (int, float)) or Tb <= 0:
    raise ValueError('The Tb parameter must be a positive number.')
  if not isinstance(Ts, (int, float)) or Ts <= 0:
    raise ValueError('The Ts parameter must be a positive number.')
  
  # Initialize the symbol mapping dictionary
  symbol_mapping = {}

  # Convert the bitstream to a list of bits
  bits = [int(b) for b in bitstream]

  # Calculate the number of symbols based on the PAM level
  num_symbols = 2 ** pam_level

  # Iterate over the range of symbols
  for symbol in range(num_symbols):
    # Convert the symbol to a binary string
    bin_str = format(symbol, 'b').zfill(len(bits))

    # If Gray coding is enabled, convert the binary string to Gray code
    if gray_code:
      bin_str = gray_encode(bin_str)

    # Map the symbol to the binary string
    symbol_mapping[symbol] = bin_str

  return symbol_mapping

def gray_encode(bin_str):
  # Initialize the Gray encoded string
  gray_str = ''

  # Iterate over the range of bits
  for i in range(len(bin_str)):
    # If this is the first bit, set the Gray encoded bit to the binary bit
    if i == 0:
      gray_bit = bin_str[i]
    # For all other bits, set the Gray encoded bit to the XOR of the previous Gray encoded bit and the current binary bit
    else:
      gray_bit = str(int(gray_str[i - 1]) ^ int(bin_str[i]))
    # Append the Gray encoded bit to the Gray encoded string
    gray_str += gray_bit

  return gray_str

# Example usage
bitstream = '0101'
pam_level = 2
k = 4
Tb = 1.0
Ts = 2.0
symbol_mapping = generate_pam_symbol_mapping(bitstream, pam_level, k, Tb, Ts)
print(symbol_mapping)  # Output: {0: '0000', 1: '0101', 2: '0110', 3: '1111', ...}
