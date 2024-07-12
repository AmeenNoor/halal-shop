document.addEventListener('DOMContentLoaded', function () {
    var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim();
    var clientSecret = document.getElementById('id_client_secret').textContent.trim();

    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    var style = {
        base: {
            color: '#32325d',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    var card = elements.create('card', { style: style });
    card.mount('#card-element');

    card.addEventListener('change', function(event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            errorDiv.textContent = event.error.message;
        } else {
            errorDiv.textContent = '';
        }
    });

    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;

        var loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay) {
            loadingOverlay.classList.remove('hidden');
        }

        document.getElementById('payment-form').classList.add('hidden');

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                errorDiv.textContent = result.error.message;

                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;

                if (loadingOverlay) {
                    loadingOverlay.classList.add('hidden');
                }

                document.getElementById('payment-form').classList.remove('hidden');
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    var clientSecretInput = document.createElement('input');
                    clientSecretInput.setAttribute('type', 'hidden');
                    clientSecretInput.setAttribute('name', 'client_secret');
                    clientSecretInput.setAttribute('value', clientSecret);
                    form.appendChild(clientSecretInput);

                    form.submit();
                }
            }
        });
    });
});
