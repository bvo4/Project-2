import React, { useState } from "react";
import styled from "styled-components";
import "./App.css"

// Watch the Button tutorial
// http://react.school/ui/button

// Free React training
// http://react.school/join

// Free Material-UI template
// http://react.school/material-ui/templates

const theme = {
  blue: {
    default: "#3f51b5",
    hover: "#283593"
  },
  pink: {
    default: "#D0312D",
    hover: "#ad1457"
  }
};



const Button = styled.button`
  background-color: ${(props) => theme[props.theme].default};
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  outline: 0;
  text-transform: uppercase;
  display: flex;
  flexDirection: 'row';
  alignItems: 'center'; //This will center your button
  marginLeft: 20;
  justifyContent: 'space-evenly';
  margin: 10px 0px;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  transition: ease background-color 250ms;
  &:hover {
    background-color: ${(props) => theme[props.theme].hover};
  }
  &:disabled {
    cursor: default;
    opacity: 0.7;
  }
`;
Button.defaultProps = {
  theme: "blue"
};


const ButtonToggle = styled(Button)`
  opacity: 0.7;
  ${({ active }) =>
    active &&
    `
    opacity: 1; 
  `}
`;

const Tab = styled.button`
  padding: 10px 30px;
  cursor: pointer;
  opacity: 0.6;
  background: white;
  flexDirection: 'row';
  justifyContent: 'space-between'
  border: 0;
  outline: 0;
  border-bottom: 2px solid transparent;
  transition: ease border-bottom 250ms;
  ${({ active }) =>
    active &&
    `
    border-bottom: 2px solid black;
    opacity: 1;
  `}
`;


export default function App() {
  // make terminal flag

  const [questionsList, setQuestionsList] = useState({
    0: {question: 'Do you want a scheme that is old and battle-tested, or new and possibly experimental?', terminal: false, no: 1, yes: 2},
    1: {question: 'Do you want a scheme that is simple to compute?', terminal: false, no: 3, yes: 4},
    2: {question: 'Are you willing to sacrifice speed for better security?', terminal: false, no: 5, yes: 6},
    3: {question: 'Are you willing to sacrifice speed for better security?', terminal: false, no: 7, yes: 8},
    4: {question: 'Simon', terminal: true},
    5: {question: 'Are you encrypting on a resource constrained device?', terminal: false, no: 9, yes: 10},
    6: {question: 'AES', terminal: true},
    7: {question: 'IDEA', terminal: true},
    8: {question: 'Threefish', terminal: true},
    9: {question: 'Are you encrypting on a memory constrained device?', terminal: false, no: 11, yes: 12},
    10: {question: 'AES', terminal: true},
    11: {question: 'AES', terminal: true},
    12: {question: 'Triple DES', terminal: true},
  });
  
  const schemeDescription = {
    'Triple DES': {description: 'Triple DES is the oldest of the five symmetric block cipher schemes.  Due to its old nature, it uses small key lengths and block sizes which has unfortunately left Triple DES obsolete and vulnerable to attacks.  While it is still accepted and used by antediluvian software, a birthday attack has been discovered, prompting the National Institute of Standards and Technology (NIST) to officially deprecate Triple DES by 2023.'},
    AES: {description: 'AES is widely considered the standard choice for encryption schemes being efficient and effective in its performance and security.   Its non-linearity and high diffusion have been achieved through its 10-round operation despite using simple mathematical operations and single encryption and decryption key'},
    IDEA: {description: 'IDEA can be described as the more complex counterpart to AES being conceptualized in 1991 but officially designed and patented sometime between 2000 and 2004. IDEA is now more accessible to use since its patent expired in 2012, allowing for official implementation aside from potential licensing issues.  IDEA uses 8.5 operations where the last round finishes halfway to undo a previous operation’s swap mechanic.  Despite being designed for more complex algorithms, IDEA costs less memory than AES, operating for fewer rounds'},
    SIMON: {description: 'SIMON is the most recently designed algorithm, created in 2013 with the creation being recognized as controversial due to the reputation of its creation by the NSA.  Regardless, SIMON was cited to be as lightweight as possible while allowing for an acceptable amount of security being an encryption scheme that operates for 44 rounds using a 128 key length.  Because of this design, SIMON is able to run effectively on low-end hardware that struggles to run even AES.'},
    Threefish: {description: 'Threefish is a recently designed algorithm relative to the rest of the block cipher schemes presented, being created in 2008 based on the Skein hash function.  Threefish was created as a successor to Twofish, an encryption scheme that competed against AES and lost.  Unlike the other encryption schemes, Threefish was designed with a much larger focus on security with number of brute force operations to crack Threefish being 2^222 operations needed, an additional  * 2^100 operations needed than the rest of the encryption schemes, giving Threefish-1024 the most potential to have the strongest security compared to the other schemes.'},
  }
  
  const [questionPtr, setQuestionPtr] = useState(0);

  function updateQuestion(selection) {
	let node = questionsList[questionPtr];
    var new_ptr;
    if (selection) {
      new_ptr = node.yes
    }
    else {
      new_ptr = node.no
    }
    
    setQuestionPtr(new_ptr);
  }

  function renderButtons() {
    let terminal = questionsList[questionPtr].terminal;
	console.log(questionPtr);
    if (terminal) {
		
		let scheme = questionsList[questionPtr].question;
		
		return (
		
		  <div class="SolutionDiv btnDiv my-btn-group width">
		  {
			  schemeDescription[scheme].description
		  }
		  
		  
          </div>
		)

    }
    else {
      return (
	  
        <div class="btnDiv my-btn-group">
            <div class = "demo">
				<span>
					<Button theme="pink" onClick={() => updateQuestion(false)}>No</Button>
				</span>
			</div>
            <div>
				<span>
				<Button onClick={() => updateQuestion(true)}>
				  Yes
				</Button>
			</span>
          </div>
        </div>
      )
    }
  }

  return (
  <div class = "outer">
    <h1 style={{textAlign: "center"}}>
    CS6903 Project
    </h1>
    
    <body style={{textAlign: "center"}}>
    Here is where the questions regarding to what cryptographic primitve you want will be asked.
    </body>
    
    <p style={{textAlign: "center"}}><strong>
      {questionsList[questionPtr].question}
    </strong></p>
    
    {renderButtons()}
  </div>
  );
}
