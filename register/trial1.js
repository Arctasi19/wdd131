// Variables
const addParticipantButton = document.querySelector("#add")
const submitButton = document.querySelector("#submitButton")
const form = document.querySelector("#registrationForm")
const summaryBlock = document.querySelector("#summary")
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
              <input id="fee-${count}" type="number" name="fee-${count}" />
            </div>
            <div class="item">
              <label for="date-${count}">Desired Date <span>*</span></label>
              <input id="date-${count}" type="date" name="date-${count}" />
            </div>
            <div class="item">
              <p>Grade</p>
              <select>
                <option selected value="" disabled selected></option>
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
function addParticipant() {
    participantCount++;
    const newParticipantHTML = participantTemplate(participantCount);
    const addButton = document.querySelector("#add");
    addButton.insertAdjacentHTML("beforebegin", newParticipantHTML);
}

function handleSubmit(event) {
    event.preventDefault();
    const totalFee = totalFees();

    const adultNameInput = document.querySelector("#adultName");
    const adultName = adultNameInput ? adultNameInput.value : "Registered Adult";
    
    form.computedStyleMap.display = "none";
    summaryBlock.computedStyleMap.display = "block";
    const message = `Thank you, ${adultName}, for registering ${participantCount} participant(s). The total fee is $${totalFee.toFixed(2)}.`;
    summaryBlock.innerHTML = message;
}

function totalFees() {
// the selector below lets us grab any element that has an id that begins with "fee"
    let feeElements = document.querySelectorAll("[id^=fee]");
    console.log(feeElements);
// querySelectorAll returns a NodeList. It's like an Array, but not exactly the same.
// The line below is an easy way to convert something that is list-like to an actual Array so we can use all of the helpful Array methods...like reduce
// The "..." is called the spread operator. It "spreads" apart the list, then the [] we wrapped it in inserts those list items into a new Array.
    feeElements = [...feeElements];
// sum up all of the fees. Something like Array.reduce() could be very helpful here :) Or you could use a Array.forEach() as well.
// Remember that the text that was entered into the input element will be found in the .value of the element.
    const total = feeElements.reduce((total, element) => {
        const fee = parseFloat(element.value) || 0;
        return total + fee;
    }, 0);
    return total;
// once you have your total make sure to return it!

}

// Event Listeners
addParticipantButton.addEventListener("click", addParticipant)
submitButton.addEventListener("submit", handleSubmit)