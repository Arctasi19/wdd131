// Variables
const addParticipantButton = document.querySelector("#add");
const submitButton = document.querySelector("#submitButton");
const form = document.querySelector("form"); 
const summaryElement = document.querySelector("#summary"); 
let participantCount = 1;

// Functions
function participantTemplate(count) {
    return `
      <section class="participant${count}">
        <p>Participant ${count}</p>
        <div class="item">
          <label for="fname-${count}"> First Name<span>*</span></label>
          <input id="fname-${count}" type="text" name="fname-${count}" value="" required />
        </div>
        <div class="item activities">
          <label for="activity-${count}">Activity #<span>*</span></label>
          <input id="activity-${count}" type="text" name="activity-${count}" />
        </div>
        <div class="item">
          <label for="fee-${count}">Fee ($)<span>*</span></label>
          <input id="fee-${count}" type="number" name="fee-${count}" value="0" />
        </div>
        <div class="item">
          <label for="date-${count}">Desired Date <span>*</span></label>
          <input id="date-${count}" type="date" name="date-${count}" />
        </div>
        <div class="item">
          <p>Grade</p>
          <select name="grade-${count}">
            <option selected value="" disabled></option>
            <option value="1">1st</option>
            <option value="2">2nd</option>
            <option value="3">3rd</option>
            <option value="4">4th</option>
            <option value="5">5th</option>
            <option value="6">6th</option>
            <option value="7">7th</option>
            <option value="8">8th</option>
            <option value="9">9th</option>
            <option value="10">10th</option>
            <option value="11">11th</option>
            <option value="12">12th</option>
          </select>
        </div>
      </section>
    `;
}

function totalFees() {
    let feeElements = document.querySelectorAll("[id^=fee]");
    feeElements = [...feeElements];
    const total = feeElements.reduce((total, element) => {
        const fee = parseFloat(element.value) || 0;
        return total + fee;
    }, 0); 

    return total;
}

function addParticipant() {
    participantCount++;
    const newParticipantHtml = participantTemplate(participantCount);
    const addButton = document.querySelector("#add");
    addButton.insertAdjacentHTML('beforebegin', newParticipantHtml);
}


function handleSubmit(event) {
    event.preventDefault();

    const totalFee = totalFees();


    const adultNameInput = document.querySelector("#adult_name");
    const adultName = adultNameInput ? adultNameInput.value : "Registered Adult";

    form.style.display = 'none';
    summaryElement.style.display = 'block'; 
    
    const message = `Thank you ${adultName} for registering. You have registered ${participantCount} participant(s) and owe $${totalFee.toFixed(2)} in Fees.`;
    summaryElement.innerHTML = `<p>${message}</p>`;
}

// Event Listeners
addParticipantButton.addEventListener("click", addParticipant); 
form.addEventListener("submit", handleSubmit);
